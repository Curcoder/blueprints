from flask import Blueprint

api = Blueprint('api', __name__, template_folder='templates', url_prefix='/api')

users = [
	{
		"name": "Jurgen",
		"job": "tester",
		"age": 40
	},
{
		"name": "raylie",
		"job": "developer",
		"age": 38
	}
]


@api.route('/get_data', methods=['GET'])
def get():
	return {'result': 'Some fucking data'}


@api.route('/user', methods=['GET'])
def user():
	result = []
	for user in users:
		result.append({
			'name': user['name'],
			'job': user['job'],
			'age': user['age']
		})
	return {"data": result}