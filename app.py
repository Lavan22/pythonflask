from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data store
data_store = {}

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Use the POST method to receive user data
@app.route('/api/user', methods=['GET','POST'])
def form_example():
    # Get JSON data from the request
    data = request.get_json()

    # Check if the data is None
    if data is None:
        return jsonify({'error': 'No data received'}), 400

    # Extract individual fields
    name = data.get('name')
    age = data.get('age')
    address = data.get('address')

    # Validate the required fields
    if not name or not age or not address:
        return jsonify({'error': 'Missing name, age, or address'}), 400

    # Optionally, you can save the data to a store or process it here
    # For example, storing it in the data_store dictionary
    data_store[name] = {'age': age, 'address': address}

    # Log the received values (optional)
    print(f"Received Name: {name}, Age: {age}, Address: {address}")

    # Respond with a success message
    return jsonify({'message': 'User saved successfully!', 'data': data_store[name]}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
