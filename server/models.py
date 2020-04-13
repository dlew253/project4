from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_cors import CORS

app=Flask(__name__)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/remindme'
app.config['SECRET_KEY'] = 'AnANGRYgoblinWASherE'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

db = SQLAlchemy(app)
app.app_context().push()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL')))
    posts = db.relationship('Post', lazy=True)

    def __repr__(self):
      return f'User(email="{self.email}", firstname="{self.firstname}", lastname="{self.lastname}")'
    def as_dict(self):
        user_dict = {
            'id': self.id,
            'email': self.email,
            'firstname': self.firstname,
            'lastname': self.lastname
        }
    def as_dict(self):
        user_dict = {c.firstname: getattr(self, c.firstname) for c in self.__table__.columns}
        del user_dict['password']
        return user_dict

    def set_password(self, password):
        self.password = pwd_context.encrpyt(password)
    
    def verify_password(self, typed_password):
        return pwd_context.verify(typed_password, self.password)

    def generate_token(self, expiration=60*5):
        s = Serializer(app.config['SECRET-KEY'], expires_in=expiration)
        return s.dumps({'id':self.id})


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True, nullable=False)
    date = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'))
    body = db.Column(db.String(2000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', onDelete='SET NULL'), nullable='false')

    def __repr__(self):
      return f'Post(id={self.id}, title={self.title}, date={self.date}, user_id={self.user_id})'

    def as_dict(self):
      return {c.name: getattr(self, c.name) for c in self.__table__.columns}


def get_or_create(model, defaults=None, **kwargs):
    instance = db.session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        params = dict((k, v) for k, v in kwargs.items())
        params.update(defaults or {})
        instance = model(**params)
        db.session.add(instance)
        db.session.commit()
        return instance, True