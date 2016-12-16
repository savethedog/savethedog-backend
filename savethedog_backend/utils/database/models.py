import binascii
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "auth_user"
    id = db.Column("id", db.Integer, primary_key=True)
    password = db.Column("password", db.String)
    username = db.Column("username", db.String)
    last_login = db.Column("last_login", db.TIMESTAMP)
    email = db.Column("email", db.String)


class Announce(db.Model):
    __tablename__ = "rottweiler_announce"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    is_active = db.Column("is_active", db.BOOLEAN)
    description = db.Column("description", db.String)
    date_creation = db.Column("date_creation", db.DATETIME)
    date_found = db.Column("date_found", db.DATETIME, nullable=True)
    latitude = db.Column("latitude", db.Float)
    longitude = db.Column("longitude", db.Float)

    @staticmethod
    def create_new_announce(description, latitude, longitude, date_creation,
                            date_found=None, is_active=True):
        try:
            new_announce = Announce(description=description, latitude=latitude,
                                    longitude=longitude, date_creation=date_creation,
                                    date_found=date_found, is_active=is_active)
            db.session.add(new_announce)
            db.session.commit()
            return new_announce
        except Exception as ex:
            print ex.message

        return None



class Token(db.Model):
    __tablename__ = "authtoken_token"
    key = db.Column("key", db.String, primary_key=True)
    created = db.Column("created", db.TIMESTAMP)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey('auth_user.id'))

    def __init__(self, key, created, user_id):
        self.key = key
        self.created = created
        self.user_id = user_id

    @staticmethod
    def generate_token(user_id):

        from datetime import datetime
        new_hash = binascii.hexlify(os.urandom(20)).decode()

        if Token.query.filter_by(user_id=user_id).first():
            Token.query.filter_by(user_id=user_id).update(dict(key=new_hash, created=datetime.now()))
        else:
            token = Token(key=new_hash, created=datetime.now(), user_id=user_id)
            db.session.add(token)

        db.session.commit()
        return new_hash
