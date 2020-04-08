from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from __init__ import Myapp
app = Myapp()
app.app_context().push()
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)

    posts = db.relationship('Post', lazy=True)
    pass
    def __repr__(self):
      return 'User(id="{self.id}", email="{self.email}", name="{self.name}")'

post_tags = db.Table('post_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True)
)

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(150), unique=True, nullable=False)
    date = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'))
    body = db.Column(db.String(2000), nullable=False)
#figure out what the fuck tags to//ok i think i got it now
    tags = db.relationship('Tag', secondary=post_tags, lazy='subquery',
        backref=db.backref('posts', lazy=True))

    def __repr__(self):
      return f'User(id={self.id}, email="{self.email}", display_name="{self.display_name}")'

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
      return f'Tag(id={self.id}, tag="{self.tag}")'