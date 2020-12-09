from app import app
from flask import render_template, url_for
from app.forms import RegistrationForm, LoginForm


app.config['SECRET_KEY'] = 'f5aa814a0c779d597472cc09c8ef33e8'


@app.route("/")
def index():
    return render_template('public/home.html')


@app.route("/about")
def about():
    return render_template('public/about.html', title="About Page")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    
    return render_template('public/register.html', title="Register", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('public/login.html', title="Login", form=form)
