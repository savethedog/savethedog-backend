from time import timezone

from utils.interfaces.authenticator import Authenticator
from utils.database.models import Token, User
from datetime import datetime

class TokenAuthenticator(Authenticator):

    def authenticate(self, auth_data):
        try:
            token_string = auth_data["token"]
            token = Token.query.filter_by(key=token_string).first()
            now = self.pg_utcnow()
            diff = now - token.created

            print diff.days

            if diff.days < 1:
                return User.query.filter_by(id=token.user_id).first()
        except Exception as ex:
            print ex.message
            return None

        return False

    def pg_utcnow(self):
        import psycopg2
        return datetime.utcnow().replace(
            tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None))







