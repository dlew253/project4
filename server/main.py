from flask import Flask, jsonify, request, g
from flask_sqlalchemy import SQLAlchemy
from models import app, User, Post, get_or_create
from crud.user_crud import get_user, create_user, update_user
from crud.post_crud import get_all_posts, get_user_posts, get_post, create_post, update_post, destroy_post
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from flask_httpauth import HTTPTokenAuth

auth = HTTPTokenAuth('Bearer')

@app.errorhandler(Exception)
def unhandled_exception(e):
    app.logger.error(f'Unhandled Exception: {e}')
    return jsonify(error=f'Server Error: {e}', message=f'Server Error: {e}')

@auth.verify_token
def verify_token(token):
    s = Serializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
        g.user = User.query.filter_by(id=data["id"]).first()
    except SignatureExpired:
        print("ERROR: signature expired")
        return False
    except BadSignature:
        print("ERROR: invalid signature")
        return False
    return True

@app.route('/auth/login', methods=['POST'])
def authenticate():
    if request.json['email'] is None or request.json['password'] is None:
        raise KeyError('Email and Password required')

    user = User.query.filter_by(email=request.json['email']).first()

    if not user or not user.verify_password(request.json['password']):
        raise Exception("Unauthorized")
    
    g.user = user
    token = user.generate_token()
    return jsonify(user=user.as_dict(), token=token.decode('ascii'), status_code=200)

@app.route('/auth/signup', methods=['POST'])
def signup():
    return create_user(**request.json)

@app.route('/api/protected')
@auth.login_required
def get_resource():
  return jsonify({ 'data': 'Hello, %s!' % g.user.name })

@app.route('/posts')
def posts_get():
    # get all public posts for homepage
    return get_all_posts()

@app.route('/posts/<int:id>')
def post_get_one(id):
    # get a post
    return get_post(id)

@app.route('/users/<int:id>')
def user_get_one(id):
    return get_user(id)

@app.route('/profile/<int:user_id>', methods=['GET', 'POST', 'PUT'])
@auth.login_required
def poems_user_get_post(user_id):
    if request.method == 'GET':
        #get user posts
        return get_user_posts(user_id)
    if request.method == 'POST':
        #post a new post
        return create_post(
            title=request.json['title'],
            date=request.json['date'],
            user_id=user_id
        )
    if request.method == 'PUT':
        # edit user profile
        return update_user(
            id=user_id,
            email=request.form['email'],
            name=request.form['name'],
            password=request.form['password']
        )

@app.route('/posts/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@auth.login_required
def post_post_put_delete(id):
    if request.method == 'PUT':
        # edit the post
        return update_post(
            id=id,
            title=request.json['title'],
            text=request.json['text']
        )
    if request.method == 'DELETE':
        # delete the post
        return destroy_post(id)

