from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('Login.js')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Error, incorrect information provided. 2 more attempts and you will die.')
        return redirect(url_for('auth.Login'))

    login_user(user, remember=remember)

    return redirect(url_for('main.Home'))

@auth.route('/signup')
def signup():
    return render_template('Signup.js')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    password = request.form.get('password')
    firstname = request.form.get('first name')
    lastname = request.form.get('last name')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists.')
        return redirect(url_for('auth.login'))

    new_user = User(email='email', password=generate_password_hash(password, method='sha256'), firstname='firstname', lastname='lastname')

    db.session.add(new_user)
    db.session.commit()
#this might throw an issue
    return redirect(url_for('main.Home'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.Landing'))