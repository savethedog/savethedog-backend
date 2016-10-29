from utils.interfaces.authenticator import Authenticator


class TokenAuthenticator(Authenticator):

    def authenticate(self, auth_data):
        return Authenticator.authenticate(self, db, auth_data)