from datetime import datetime
from flask import jsonify, request
from flask_restful import Resource, abort
import pymongo
from pymongo import MongoClient
from flask_restful import reqparse
from sqlalchemy.orm import class_mapper

from utils.database.models import Announce
from utils.database.retrievers import MongoObjectsRetriever
from utils.request.parser import NewAnnounceRequestParser


class NearLocationResource(Resource):
    def __init__(self, authenticator, mongo):
        self.authenticator = authenticator
        self.mongo = mongo

        # TODO: move these objects in the resource call
        self.retriever = MongoObjectsRetriever()
        self.parser = NewAnnounceRequestParser()

    def get(self, token):
        # if not self.authenticator.authenticate(auth_data=dict(token=token)):
        #     abort(401)

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

    def post(self, token):

        # if not self.authenticator.authenticate(auth_data=dict(token=token)):
        #     abort(401)
        parsed_data = self.parser.parse(request)

        if not parsed_data.get('date_created'):
            return jsonify({'error': 'Missing creation date', 'success': False})

        converted_date = datetime.strptime(parsed_data.get('date_created'), '%d/%m/%Y %H:%M:%S')
        res = Announce.create_new_announce(parsed_data.get('description'), parsed_data.get('latitude'),
                                           parsed_data.get('longitude'), converted_date)
        return jsonify(object_to_dict(res))


def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))

    return d


def object_to_dict(obj):
    if not obj:
        return None

    columns = [column.key for column in class_mapper(obj.__class__).columns]
    get_key_value = lambda c: (c, getattr(obj, c).isoformat()) if isinstance(getattr(obj, c), datetime) else (
    c, getattr(obj, c))
    return dict(map(get_key_value, columns))
