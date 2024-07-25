from flask import Flask, request, jsonify

from StudentService import user_service
from Student import Student

app = Flask(__name__)

service = user_service()

@app.route('/user', methods = ['POST'])
def create_student():
    data = request.get_json() 
    user = Student(data['id'], data['email'], data['password'],  data['username'])
    service.create_user(user) 
    doc_json = Student.to_json(user)
    print("doc json ", doc_json)
    return doc_json 


@app.route('/users', methods = ['GET'])
def get_all_users():
    users_list = service.get_users()
    return users_list

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = service.get_user(user_id)
    return user

@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    service.delete_user(user_id)
    return jsonify({'message': 'User deleted successfully', 'id': user_id})

@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = Student(user_id, data['email'], data['password'], data['username'])
    service.update_user(user)
    return jsonify({'message': 'User updated successfully', 'id': user_id})


@app.route('/')
def hello():
    return 'Your Flask Server Running'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = '5001')

