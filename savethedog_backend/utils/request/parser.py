from datetime import datetime
from flask.ext.restful import reqparse


class NewAnnounceRequestParser:
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('latitude', type=float)
        self.parser.add_argument('longitude', type=float)
        self.parser.add_argument('description', type=str)
        self.parser.add_argument('date_created', type=str)

    def parse(self, request):
        return self.parser.parse_args(req=request)
