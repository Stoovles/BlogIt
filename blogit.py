from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

@app.route('/')
def default():
    return "Root Page"


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have successfully logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Check username and/or password', 'danger')
    return render_template('login.html', title='Login', form=form)
