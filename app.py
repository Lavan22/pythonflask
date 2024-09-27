from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
# Sample data store
data_store = {}

# Use the POST and GET method for creative form.
@app.route('/api/user', methods=['POST', 'GET'])
def form_example():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form['age']
        address = request.form['address']
        return '<h1> The language is {}. The framework is {}.</h1>'.format(name, age, address)
    return '''<form method="POST" action="">
    Language <input types="text" name="language">
    Framework <input type="text" name="framework">
    <input type="submit">
    </form>'''

if __name__ == '__main__':
    app.run(debug=True)
