from utils.interfaces.authenticator import Authenticator
from utils.database.models import User


class HashedPasswordAuthenticator(Authenticator):

    def authenticate(self, auth_data):

        if not isinstance(auth_data, dict):
            raise Exception("auth_data must be a dictionary")

        username = auth_data['username']
        passowrd = auth_data['password']
        try:
            user = User.query.filter_by(username=username).first()
        except:
            return False

        return self.get_hashed_password(passowrd, user.password)

    def get_hashed_password(self, raw_password, hash):
        from passlib.hash import django_pbkdf2_sha256 as hasher
        return hasher.verify(raw_password, hash)
