from flask_restplus import Resource
from flask import request, jsonify
from email_validator import validate_email

from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email

from app.main.util.dto import UserDto

api = UserDto.api
_user = UserDto.user

user_details = []

@api.route('/')
class Registration(Resource):

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        username = StringField(data['username'], validators=[Length(min=5, max=10)])
        email = StringField(validate_email(data['email']))
        password = PasswordField(data['password'], validators=[DataRequired()])
        user_details.append((username, email, password))
        print(user_details)
        response_body = {'status': 'success',
                         'message': 'User created successfully'}
        return response_body, 201

