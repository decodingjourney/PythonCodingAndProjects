from flask_jwt_extended import jwt_required, get_raw_jwt, get_jwt_claims
from flask_restplus import Resource, reqparse
from app.main.service.auth_helper import Auth
from app.main.util.dto import UserDto
from blacklist import Blacklist
from app.main.util.dto import authorizations



api = UserDto.api
_user = UserDto.user
login_user = UserDto.login_user
delete_user = UserDto.delete_user

user_details = []

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('email',
                          type=str,
                          required=True,
                          help='This field can not be blank'
                          )
_user_parser.add_argument('username',
                          type=str,
                          required=False,
                          help='This field can not be blank'
                          )
_user_parser.add_argument('password',
                          type=str,
                          required=True,
                          help='This field can not be blank')

# Blacklist = set()

@api.route('/signup')
class Registration(Resource):

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user', security=None)
    def post(self):
        """Creates a new User """
        data = _user_parser.parse_args()
        return Auth.signup_user(data)

    @api.route('/login')
    class UserLogin(Resource):
        @api.expect(login_user, validate=True)
        @api.response(200, 'User successfully logged in.')
        @api.doc('User Login', security=None)
        def post(self):
            """User Login """
            data = _user_parser.parse_args()
            return Auth.login_user(data)

    @api.route('/logout')
    class UserLogout(Resource):
        @api.doc(security='jwt_token')
        @api.response(200, 'User Successfully Logged out')
        @jwt_required
        def post(self):
            """User Logout """
            jti = get_raw_jwt()['jti']
            Blacklist.add(jti)
            return {"message": "You Successfully logged out! Please login"}, 200


    @api.route('/delete')
    class DeleteUser(Resource):
        @api.expect(delete_user, validate=True)
        @api.doc(security='jwt_token')
        @api.response(200, 'User Deleted Successfully')
        @jwt_required
        def delete(self):
            """remove specific user """
            _user_parser = reqparse.RequestParser()
            _user_parser.add_argument('email',
                                      type=str,
                                      required=True,
                                      help='This field can not be blank'
                                      )

            data = _user_parser.parse_args()
            claims = get_jwt_claims()
            if not claims['is_admin']:
                return {'message': 'Admin privilege required to delete the user.'}, 401
            return Auth.deleteUser(data)












