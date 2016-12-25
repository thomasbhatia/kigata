from app.contrib.mongotalk import MongoTalk
import datetime
from marshmallow import Schema, fields, ValidationError, validates_schema
from flask import current_app, jsonify
from bson import ObjectId
from app.helpers import generate_sid
from app.contrib.mongotalk import mongodb


class User(MongoTalk):
    collection = mongodb.db.users
    now = datetime.datetime.now()

    def __unicode__(self):
        return self.person_id

    @classmethod
    def get_json(cls):
        user_schema = UserSchema()
        data, errors = user_schema.dump(cls)
        if not errors:
            response = dict(status='success', data=data)
        else:
            response = dict(status='error', data=errors)
        return jsonify(response), 200

    @classmethod
    def set_active(cls, *args):
        if args:
            data = dict(is_actice=args[0])
            cls.set(data)

    @classmethod
    def update_passwd(cls, *args):
        if args:
            data = dict(secret=args[0])
            cls.set(data)

    @classmethod
    def is_admin(cls):
        if hasattr(cls, 'is_admin'):
            if cls.is_admin is True:
                return True

    @classmethod
    def create_user(cls, *args):
        json_data = args[0]
        user_schema = UserSchema()
        data, errors = user_schema.load(json_data)
        if errors:
            response = dict(status='error', error=errors)
            current_app.logger.debug(response)
            return jsonify(response), 422
        constants = dict(is_active=False,
                         last_accessed = cls.now,
                         date_joined = cls.now,
                         shared_secret_renewal_interval=21600,  # 6 hours
                         time_to_renew_shared_secret=0,
                         get_settings=False,
                         secret=generate_sid()
                         )
        data.update(constants)
        # Check if user is unique
        if cls.get({'email': data['email']}):
            response = dict(status='error', error=dict(email='Not unique'))
            return jsonify(response), 409
        else:
            user = cls(data)
            user.save()
            new_user = User.get({'_id': ObjectId(user.id)})
            current_app.logger.warn(new_user.email)
            data, errors = user_schema.dump(new_user)
            response = dict(status='success', data=data)
            return jsonify(response), 201

    @classmethod
    def update_user_json(cls, *args):
        fields_allowed_to_update = ('first_name', 'last_name', 'secret', 'email')
        data = args[0]
        user_schema = UserSchema(only=fields_allowed_to_update)
        user_data, errors = user_schema.load(data, partial=True)
        if errors:
            response = jsonify(dict(status='error', data=errors)), 400
            current_app.logger.debug(response)
        else:
            cls.set(data)
            response = jsonify(dict(status='success', data='ok')), 202
        return response


# User Schema
class UserSchema(Schema):
    _id = fields.Str(dump_only=True, required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    is_active = fields.Boolean()
    last_accessed = fields.DateTime()
    date_joined = fields.DateTime(dump_only=True)
    secret = fields.Str(load_only=True)
    email = fields.Email(required=True)

    @validates_schema(pass_original=True)
    def check_unknown_fields(self, data, original_data):
        for key in original_data:
            if key not in self.fields:
                raise ValidationError(['Unknown field name'], format(key))

    @validates_schema(pass_original=True)
    def check_empty_fields(self, data, original_data):
        for key, value in original_data.iteritems():
            if value == '' or not value:
                raise ValidationError(['Empty value for field name'], format(key))
