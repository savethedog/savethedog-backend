from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
# todo create string from config file
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://savethedog:savethedog@localhost/savethedog'

if __name__ == '__main__':
    app.run(debug=True)