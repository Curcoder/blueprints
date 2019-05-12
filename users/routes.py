from flask import Blueprint, render_template

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/login')
def login():
	return render_template('views/login.html')


@users.route('/register')
def register():
	return render_template('views/register.html')


