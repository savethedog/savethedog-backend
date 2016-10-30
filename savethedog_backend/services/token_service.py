from flask import jsonify
from flask_restful import reqparse, abort
from flask_restful import Resource

from utils.database.models import Token


class TokenResource(Resource):
    def __init__(self, **kwargs):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("username", type=str, required=True, location="json")
        self.reqparse.add_argument("password", type=str, required=True, location="json")
        self.authenticator = kwargs["authenticator"]

    def post(self):
        args = self.reqparse.parse_args()
        username = args["username"]
        password = args["password"]
        user = self.authenticator.authenticate(dict(username=username, password=password))

        if not user:
            abort(400)

        token = Token.generate_token(user.id)
        return jsonify(dict(token=token), 200)
