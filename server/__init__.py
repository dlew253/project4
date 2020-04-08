from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager

db = SQLAlchemy()

def Myapp():
   app = Flask(__name__)
   db = SQLAlchemy()
   app.config['SECRET_KEY'] = 'AnANGRYgoblinWASherE'
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/remindme'
   db.init_app(app)
   return Myapp

   login_manager = LoginManager()
   login_manager.login_view = 'auth.login'
   login_manager.init_app(app)

   from .models import User

   @login_manager.user_loader
   def load_user(user_id):
      return User.query.get(int(user_id))

   from .auth import auth as auth_blueprint
   app.register_blueprint(auth_blueprint)

   from .main import main as main_blueprint
   app.register_blueprint(main_blueprint)

   return Myapp

