from flask import Flask, render_template, request , flash  
import os 

app = Flask(__name__)

app.secret_key = os.urandom(16) 


user_credentials = [
    {'username': 'user1', 'password': '123456789'},
    {'username': 'user2', 'password': '098765432'},
    {'username': 'user3', 'password': '111222333'}
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if any(user['username'] == username and user['password'] == password for user in user_credentials):
            # Authentication successful
            return render_template('success.html')
        else:
            # Authentication failed
            flash('Invalid username or password')
            return render_template('index.html')

    # Render the login form for GET requests
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



