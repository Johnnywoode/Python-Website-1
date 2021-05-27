from flask import Blueprint, render_template, flash, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "this is logout page"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        fullname = request.form.get('fullname')
        password = request.form.get('password')
        cpassword = request.form.get('cpassword')

        if len(fullname) < 3:
            flash("Full name must be greater than 2 characters", category='error')
        elif len(email) < 4:
            flash("Enter a valid email", category='error')
        elif password != cpassword:
            flash("Passwords don\'t match", category='error')
        elif len(password) < 8:
            flash("Password must be at least 8 characters", category='error')
        else:
            flash("Account created successfully", category='success')

    return render_template("sign_up.html")