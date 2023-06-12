from flask import Flask, request, jsonify

app = Flask(__name__)
usernames = []

@app.route('/usernames', methods=['GET', 'POST'])
def handle_usernames():
    if request.method == 'POST':
        username = request.form.get('username')
        if username:
            usernames.append(username)
            return jsonify({'message': 'Username saved successfully'})
        else:
            return jsonify({'error': 'Invalid username'})

    if request.method == 'GET':
        return jsonify(usernames)

if __name__ == '__main__':
    app.run(port=8000)