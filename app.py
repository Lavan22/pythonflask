from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
# Sample data store
data_store = {}

@app.route('/api/user', methods=['POST'])
def post_user():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    address = data.get('address')

    if name and age and address:
        # Save user data to in-memory storage or database
        data_store[name] = {'age': age, 'address': address}
        return jsonify({'message': 'User saved successfully!'}), 201
    return jsonify({'error': 'Missing name, age, or address'}), 400

if __name__ == '__main__':
    app.run(debug=True)
