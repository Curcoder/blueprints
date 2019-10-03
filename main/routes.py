from flask import Blueprint, render_template
from api.routes import users

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def home():
	user_list = [user for user in users]
	return render_template('home.html', user_list=user_list)


@main.route('/about')
def about():
	return render_template('about.html')


