import psycopg2


class DBProvider:

    def __init__(self, config):
        self.conn = psycopg2.connect(user=config['user'],
                                     password=config['password'],
                                     database=config['database'],
                                     dsn=config['url'])
        self.cursor = self.conn.cursor()

    def get_user_from_token(self, token):
        pass
