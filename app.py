from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data store
data_store = {}

@app.route('/api/user', methods=['GET'])
def get_user():
    name = request.args.get('name')
    if name in data_store:
        return jsonify(data_store[name])
    return jsonify({'error': 'User not found'}), 404

@app.route('/api/user', methods=['POST'])
def post_user():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    address = data.get('address')
    
    if name and age and address:
        data_store[name] = {'age': age, 'address': address}
        return jsonify({'message': 'User saved successfully!'}), 201
    return jsonify({'error': 'Missing name, age, or address'}), 400

if __name__ == '__main__':
    app.run(debug=True)
