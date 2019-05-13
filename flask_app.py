from flask import Flask
from users.routes import users
from main.routes import main

app = Flask(__name__)


app.register_blueprint(main)
app.register_blueprint(users)


if __name__ == '__main__':
	app.run()
