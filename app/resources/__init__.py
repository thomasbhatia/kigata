from flask import request, jsonify, current_app
from flask.ext.classy import FlaskView, route
from app.mod_auth import login_required

# We have User and UserSchema functions here to escape the circular import hell.
def User(arg=None):
    from app.models.user import User
    return User(arg)

def UserSchema():
    from app.models.user import UserSchema
    return UserSchema()

class RestApiView(FlaskView):

    route_base = '/'

    @route('/helloworld', methods=['GET'])
    def helloworld(self):
        data = 'Hello World'
        return jsonify(data=data)

    @route('/users', methods=['POST'])
    def new_user(self, **kwargs):
        from app.models.user import UserSchema
        from app.models.user import User

        json_data = request.get_json()
        if not json_data:
            response = dict(status='error', data=dict(payload='JSON payload required'))
            return jsonify(response), 400

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
    def get_user(self, **kwargs):
        user = kwargs['user']

        user_schema = UserSchema()

        user_data, errors = user_schema.dump(user)

        current_app.logger.warn(errors)

        response = dict(status='success', data=user_data)

        return jsonify(response), 200

    @route('/users/me', methods=['PATCH'])
    @login_required
    def edit_user(self, **kwargs):
        from app.models.user import UserSchema
        from app.models.user import User

        json_data = request.get_json()
        if not json_data:
            response = dict(status='error', data=dict(payload='JSON payload required'))
            return jsonify(response), 400

        user = User.get({'email': json_data['email']})
        current_app.logger.info(user)

        if 'secret' in json_data:
		    User.update_passwd(json_data['secret'])

        response = dict(status='success', data='User updated')
        head = 200

        return jsonify(response), head
        