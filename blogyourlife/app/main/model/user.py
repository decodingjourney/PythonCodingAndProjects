import uuid
from passlib.hash import pbkdf2_sha256
from app.main import collection
from flask import jsonify, session

class UserModel():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = pbkdf2_sha256.encrypt(password)


    def signup(self):
        user = {
            "_id": uuid.uuid4().hex,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }
        collection.insert_one(user)

    @classmethod
    def find_by_email(cls, email):
        return collection.find_one({'email': email})

    @classmethod
    def delete_by_email(cls, email):
        collection.delete_one({'email': email})



