from flask_restful import Resource

class LocationResource(Resource):

    def __init__(self, db, authenticator):
        self.db = db
        self.authenticator = authenticator

    def get(self, token, latitude, longitude):

        if self.authenticator.authenticate(db=self.db, auth_data=token):
            print "pass"






