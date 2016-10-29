from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from api import app

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "auth_user"
    id = db.Column("id", db.Integer, primary_key=True)
    password = db.Column("password", db.String)
    username = db.Column("username", db.String)
    last_login = db.Column("last_login", db.TIMESTAMP)
    email = db.Column("email", db.String)


class Tokens(db.Model):
    __tablename__ = "authtoken_data"
    key = db.Column("key", db.String, primary_key=True)
    created = db.Column("created", db.TIMESTAMP)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey('auth_user.id'))
