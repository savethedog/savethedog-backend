from flask import jsonify
from flask_restful import Resource, abort


class LocationResource(Resource):

    def __init__(self, authenticator):
        self.authenticator = authenticator

    def get(self, token):

        if not self.authenticator.authenticate(auth_data=dict(token=token)):
            abort(400)

        return jsonify(dict(result="ok"))






