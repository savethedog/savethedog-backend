from pymongo import MongoClient

from utils.database.makers import MongoObjectsMaker


class MongoLandmark:
    def __init__(self, config=None):

        if not config:
            self.url = 'mongodb://localhost:27017/'
            self.db_name = 'test'
            self.collection_name = 'landmarks'
        else:
            raise NotImplemented('Dynamic config is not implemented')

        self.connection = MongoClient(self.url)
        self.db = self.connection[self.db_name]
        self.collection = self.db[self.collection_name]

    def add_location(self, announce_id, lat, long):

        if self.collection_name != 'landmarks':
            raise Exception('Wrong collection {}'.format(self.collection_name))
        return self.collection.insert_one(MongoObjectsMaker.make_announce_location(announce=announce_id,
                                                                                   lat=lat,
                                                                                   long=long)).inserted_id

    def get_narby_announces(self, latitude, longitude, radius=1):
        query = MongoObjectsMaker.make_nearby_query(latitude, longitude, radius)
        return list(self.collection.find(query))
