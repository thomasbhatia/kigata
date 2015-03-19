from app.models import Model
from app.factory import mongodb
import datetime
from marshmallow import Schema, fields, ValidationError
from flask import current_app, json
from bson import ObjectId
from app.helpers import generate_sid

now = datetime.datetime.now()

class User(Model):
    collection = mongodb.db.users

    def __unicode__(self):
        return self.person_id

    @classmethod
    def set_active(cls, *args):
        if args:
            data = dict(is_actice=args[0])
            cls.set(data)

    @classmethod
    def is_admin(cls):
        if hasattr(cls, 'is_admin'):
            if cls.is_admin is True:
                return True

    @classmethod
    def create_user(cls, *args):
        """Creates and saves a User with the given username, e-mail and password."""
        current_app.logger.warn(args)
        data = {}
        if args:
            data = args[0]

        constants = dict(is_active=False,
                         last_accessed=now,
                         date_joined=now,
                         shared_secret_renewal_interval=21600, # 6 hours
                         time_to_renew_shared_secret=0,
                         get_settings=False,
                         secret=generate_sid()
        )

        data.update(constants)
        current_app.logger.warn(data)
        user = cls(data)
        user.save()

        current_app.logger.info(user.id)

        new_user = cls.get({'_id': ObjectId(user.id)})
        return new_user

# User Schema
class UserSchema(Schema):
    _id = fields.Str(dump_only=True, required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    is_active = fields.Boolean()
    last_accessed = fields.DateTime()
    date_joined = fields.DateTime(dump_only=True)
    secret = fields.Str()

