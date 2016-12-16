class MongoObjectsMaker:
    @staticmethod
    def make_announce_location(announce, lat, long):
        return {
            'announce': announce,
            'loc': {
                'type': "Point",
                'coordinates': [lat, long]
            }
        }

    @staticmethod
    def make_nearby_query(latitude, longitude, radius):
        from math import radians
        query = {
            "loc": {
                "$geoWithin": {
                    "$center": [[latitude, longitude], radians(radius)]
                }
            }
        }
        return query
