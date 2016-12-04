from flask.ext.sqlalchemy import SQLAlchemy

from utils.database.models import Announce

db = SQLAlchemy()


class MongoObjectsRetriever:
    def __init__(self):
        self.db = db

    def get_announces(self, mongo_list):
        ids_list = list(map(lambda x: int(x['id']), mongo_list))
        return Announce.query.filter(Announce.id.in_(ids_list)).all()
