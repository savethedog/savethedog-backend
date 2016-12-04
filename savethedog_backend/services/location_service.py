from flask import jsonify
from flask_restful import Resource, abort
import pymongo
from pymongo import MongoClient
from flask_restful import reqparse

from utils.database.retrievers import MongoObjectsRetriever


class NearLocationResource(Resource):
    def __init__(self, authenticator, mongo):
        self.authenticator = authenticator
        self.mongo = mongo
        self.retriever = MongoObjectsRetriever()

    def get(self, token):
        if not self.authenticator.authenticate(auth_data=dict(token=token)):
            abort(400)

        parser = reqparse.RequestParser()
        parser.add_argument('lat')
        parser.add_argument('long')
        args = parser.parse_args()

        nearby_items = self.mongo.get_narby_announces(float(args.get('lat')), float(args.get('long')), radius=1)
        items = self.retriever.get_announces(nearby_items)
        announces = {'announces': []}

        for item in items:
            announces['announces'].append(row2dict(item))

        return jsonify(announces)

    def post(self):
        pass


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d
