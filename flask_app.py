from flask import Flask, render_template
from users.routes import users

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/about')
def about():
	return render_template('about.html')


app.register_blueprint(users)


if __name__ == '__main__':
	app.run()
