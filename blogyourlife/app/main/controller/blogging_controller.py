from flask import Request, jsonify
from flask_restplus import Resource
from app.main.util.dto import PostDto

posts = [
    {
        'author': 'Anand Kumar Jha',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 18, 2020'
    },
    {
        'author': 'Sonam Kumari',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 17, 2020'
    }
]

api = PostDto.api
_blog = PostDto.blog_details


@api.route('/')
class Home(Resource):
    @api.doc('list of your blogs')
    def get(self):
        return jsonify(posts)
