from flask import render_template, redirect, url_for, flash
from log import app_flask, db
from .models import Log, User
from .forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user


@app_flask.route('/')
def index():
    return render_template("index.html")

@app_flask.route('/logs')
def logs():
    logs_= Log.query.all()
    return render_template("logs.html", logs_=logs_)

@app_flask.route('/users')
def users():
    users_= User.query.all()
    return render_template("users.html", users=users_)

@app_flask.route('/api/logs')
def api_log():
    return jsonify(logs)

@app_flask.route('/log/<int:id_>')
def log_single(id_):
    log = Log.query.filter_by(id=id_).first()
    if log == None:
        flash(f'There is no log with id corresponding with {id_}')
    print(log)
    return render_template("about.html", log=log)

@app_flask.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create=User(username=form.username.data, email=form.email.data,
                            password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('index'))
    
    if form.errors != {}:
        for error in form.errors.values():
            flash(f'The error came from {error}')
    return render_template('register.html', form=form)

@app_flask.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(attempted_password=form.password.data):
            login_user(user)
            flash(f'You are logged in as {user.username}')
            return redirect(url_for('index'))
    else:
        flash(f'Wrong credentials')
        
    return render_template('login.html', form=form)


@app_flask.route('/logout')
def logout():
    flash(f'You have been logged out')
    logout_user()    
    return redirect(url_for('index'))