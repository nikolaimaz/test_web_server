from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
request= 0

def request_counter():
    global request
    request +=1
    return request
    
users = {
    "admin": generate_password_hash("qwerty1!"),
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/stats')
@auth.login_required
def welcome_and_stats():
    return f"Current user {auth.current_user()}<br><br>Total served requests for authenticated users {request_counter()}"
  
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')