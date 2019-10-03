from flask import Flask
from users.routes import users
from main.routes import main
from api.routes import api

app = Flask(__name__)


app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(api)


if __name__ == '__main__':
	app.run()
