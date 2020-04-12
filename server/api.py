from models import post, user
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
from flask_httpauth import HTTPTokenAuth
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

auth = HTTPTokenAuth('Bearer')

@app.errorhandler(Exception)
def unhandled_exception(e):
       app.logger.error('Unhandled Exception: %s', (e))

@auth.verify_token
def verify_token(token):
   s = Serializer(app.config['SECRET_KEY'])
   try:
      data = s.loads(token)
      g.user = User.query.filter_by(id=data['id']).first()
   except SignatureExpired:
      return False
   except BadSignature:
      return False
   return True

@app.route('/auth/login', methods=['POST'])
def authenticate():
   if request.json['email'] is None or request.json['password'] is None:
      raise KeyError("Email and password required")

   g.user = user
   token = user.generate_token()
   return jsonify(user=user.as_dict(), token=token.decode('ascii'), status_code=200)

@app.route('api/protected')

@auth.login_required
def get_resource():
   return jsonify{( 'data': 'Hello, %s!')}