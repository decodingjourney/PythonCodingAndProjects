import urllib.parse

from flask import Flask
from flask_bcrypt import Bcrypt
import pymongo
from flask_jwt_extended import JWTManager
from blacklist import Blacklist

flask_bcrypt = Bcrypt()

# Database
cluster = pymongo.MongoClient("mongodb+srv://mymongodb:"+urllib.parse.quote("Mongodb@123")+"@cluster0.kdc3k.mongodb"
                                ".net/nursery?retryWrites=true&w=majority")
db  = cluster["nursery"]
collection = db["users"]

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = b'\xcc^\x91\xea\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
    flask_bcrypt.init_app(app)
    jwt = JWTManager(app)

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        return decrypted_token['jti'] in Blacklist

    @jwt.user_claims_loader
    def add_claims_to_jwt(identity):
        if identity == 'anand@gmail.com':  # instead of hard-coding, we should read from a config file to get a list of admins instead
            return {'is_admin': True}
        return {'is_admin': False}
    return app
