from flask_restplus import Namespace, fields


authorizations = {
    'jwt_token': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

class PostDto:
    api = Namespace('blog', description='your blogs')
    blog_details =api.model('blog details', {

    })


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })

    login_user = api.model('userLogin', {
        'email': fields.String(required=True,description='email'),
        'password': fields.String(required=True, description='password')
    })

    delete_user = api.model('deleteUser', {
        'email': fields.String(required=True, description='email')
    })