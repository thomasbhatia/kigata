from functools import wraps
from flask import request, jsonify, current_app


def authenticate(authorization):
    from model import User
    import jwt

    current_app.logger.info(authorization)

    try:
        auth_method, token = authorization.split(':')
        decoded = jwt.decode(token, '', algorithm='HS256', verify=False)
    except Exception, e:
        current_app.logger.warn(e)
        return False

    email = decoded.get('email')
    current_app.logger.warn(email)

    user = User.get({'email': email})

    if user:
        current_app.logger.warn(user.secret)
        try:
            if auth_method == 'KIGATA':
                current_app.logger.info(user._id)
                jwt.decode(token, user.secret, algorithm='HS256')
            else:
                return False
        except jwt.DecodeError:
            return False
    else:
        return False
    return user


# require login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = authenticate(request.headers.get('Authorization'))
        if not user:
            response = dict(status='error', data=dict(authentication='failed'))
            return jsonify(response), 401
        else:
            kwargs['user'] = user
        return f(*args, **kwargs)
    return decorated_function
