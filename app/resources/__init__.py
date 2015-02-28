from flask import jsonify, current_app
from flask.ext.classy import FlaskView, route

class RestApiView(FlaskView):

    route_base = '/'

    @route('/helloworld', methods=['GET'])
    def helloworld(self):
        data = 'Hello World'
        return jsonify(data=data)
