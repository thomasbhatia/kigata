from flask import request, jsonify, current_app
from flask.ext.classy import FlaskView, route
from app.contrib.mod_auth import login_required
from functools import wraps


# require login
def json_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.get_json():
            response = dict(status='error', data=dict(payload='JSON payload required'))
            return jsonify(response), 400
        else:
            return f(*args, **kwargs)
    return decorated_function


class RestApiView(FlaskView):
    route_base = '/'

    @route('/helloworld', methods=['GET'])
    def helloworld(self):
        data = 'Hello World'
        return jsonify(data=data)

    @route('/users', methods=['POST'])
    @json_required
    def new_user(self, **kwargs):
        from app.contrib.mod_auth.model import User
        from app.contrib.mod_auth.model import UserSchema
        json_data = request.get_json()

        current_app.logger.info(json_data)

        user_schema = UserSchema()
        data, errors = user_schema.load(json_data)

        if errors:
            response = dict(status='error', error=errors)
            return jsonify(response), 422

        # Check if user is unique
        user = User.get({'email': data['email']})

        if user:
            response = dict(status='error', error=dict(email='Not unique'))
            return jsonify(response), 422

        current_app.logger.info(data)

        new_user = User.create_user(data)

        user_schema = UserSchema()
        user_data, errors = user_schema.dump(new_user)
        response = dict(status='success', data=user_data)

        return jsonify(response), 201

    @route('/users/me', methods=['GET'])
    @login_required
    def get(self, user):
        return user.get_jsonify()

    @route('/users/me', methods=['PATCH'])
    @login_required
    @json_required
    def update(self, user):
        json_data = request.get_json()
        return user.update_user_json(json_data)

