from flask import Flask, render_template, request , flash  
import os 

app = Flask(__name__)



user_credentials = [
    {'username': 'user1', 'password': '123456789'},
    {'username': 'user2', 'password': '098765432'},
]

@app.route('/', methods=['GET', 'POST'])
def index():
    msg = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = next((user for user in user_credentials if user['username'] == username), None)
        if user and user['password'] == password:
            return render_template('success.html')
        else:
            msg = 'Incorrect username or password. Please try again.'
            
    return render_template('index.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=True)
