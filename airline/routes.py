from airline import app, db
from flask import render_template, request, redirect, url_for
from airline.forms import SignupForm, LoginForm

from werkzeug.security import check_password_hash

from flask_login import login_user, current_user, login_required

from airline.models import User, Post
# Home Route
@app.route("/")
def home():
    posts = Post.query.all()
    return render_template("index.html", post=posts)

    # Sign Up Route


@app.route("/signup", methods=["GET", "POST"])
def signup():
    signupForm = SignupForm()
    if request.method == "POST":
        firstname = signupForm.firstname.data
        lastname = signupForm.lastname.data
        email = signupForm.email.data
        address = signupForm.address.data
        phonenumber = signupForm.phonenumber.data
        password = signupForm.password.data
        print(firstname, lastname, email, address, phonenumber, password)

        user = User(firstname, lastname, email, address, password)
        try:
            db.session.add(user)
            db.session.commit()
        except:
            print('database in use')
        return redirect(url_for('login'))
    return render_template("createaccount.html", signupform=signupForm)


# login route
@app.route("/login", methods=["GET", "POST"])
def login():
    loginForm = LoginForm()
    if request.method == "POST":
        user_email = loginForm.email.data
        password = loginForm.password.data
        # find out who the logged in user currently is
        logged_user = User.query.filter(User.email == user_email).first()
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            print(current_user.email)
            return redirect(url_for('home'))
        else:
            print("Not Valid Method")
    return render_template("login.html", loginform=loginForm)


# booking route
@app.route("/booking", methods=["GET", "POST"])
def booking():
    posts = Post.query.all()
    return render_template("booking.html", post=posts)


