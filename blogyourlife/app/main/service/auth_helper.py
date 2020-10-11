from flask_jwt_extended import create_refresh_token, create_access_token
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from app.main.model.user import UserModel


class Auth:
    @staticmethod
    def login_user(data):
        user = UserModel.find_by_email(data['email'])
        if not user:
            return {"message": "Your email is not yet registered, Please register first to Login!"}, 401
        elif user and pbkdf2_sha256.verify(data['password'], user['password']):
            access_token = create_access_token(identity=user['email'])
            refresh_token = create_refresh_token(user['email'])
            response_object = {
                   'status': 'success',
                   'message': 'Successfully logged in.',
                   'access': access_token,
                   'refresh': refresh_token
               }

            return response_object, 200

        return {"message": "Invalid Credentials!, Either email or passwords is incorrect"}, 401
    @staticmethod
    def signup_user(data):
        user = UserModel(username=data['username'], email=data['email'], password=data['password'])
        if UserModel.find_by_email(data['email']):
            return {"message": "A user with that email already exists"}, 400
        user.signup()
        response_body = {'status': 'success',
                         'message': 'User created successfully'}
        return response_body, 201

    @staticmethod
    def deleteUser(data):
        user = UserModel.find_by_email(data['email'])
        if not user:
            return {"message": "User is not in our database"}, 401

        UserModel.delete_by_email(user['email'])
        return {'message': 'user deleted successfully from our database'}, 200


