from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@app.route('/')
def home():
    return render_template('Landing.js')

@app.route('/home')
def profile():
    return render_template('Home.js')