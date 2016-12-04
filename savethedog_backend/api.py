from flask import Flask
from flask_restful import Api
from services.token_service import TokenResource
from services.location_service import NearLocationResource
from utils.database.mongo import MongoLandmark
from utils.implementations.token_authenticator import TokenAuthenticator
from utils.implementations.hashed_password_authenticator import HashedPasswordAuthenticator
from utils.database.models import db


app = Flask(__name__)
api = Api(app)
# todo create string from config file
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://savethedog:savethedog@localhost/savethedog'
db.init_app(app)

api.add_resource(TokenResource, "/api/login/",
                 resource_class_kwargs=dict(authenticator=HashedPasswordAuthenticator()))

api.add_resource(NearLocationResource, "/api/location/<string:token>/",
                 resource_class_kwargs=dict(authenticator=TokenAuthenticator(),
                                            mongo=MongoLandmark()))


if __name__ == '__main__':
    app.run(debug=True)