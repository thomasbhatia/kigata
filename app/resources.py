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
    def post(self):
        """Required values: first_name, last_name, email"""
        from app.contrib.mod_auth.model import User
        json_data = request.get_json()
        return User.create_user(json_data)

    @route('/users/me', methods=['GET'])
    @login_required
    def get(self, user):
        return user.get_json()

    @route('/users/me', methods=['PATCH'])
    @login_required
    @json_required
    def patch(self, user):
        json_data = request.get_json()
        return user.update_user_json(json_data)

