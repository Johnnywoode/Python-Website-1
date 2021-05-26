from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<h1>This is login page</h1>"

@auth.route('/logout')
def logout():
    return "<h1>This is logout page</h1>"

@auth.route('/sign-up')
def sign_up():
    return "<h1>This is signup page</h1>"
