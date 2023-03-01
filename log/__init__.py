"""
You can interact with the database in a shell by either of the following methods:

    First method
        Instead of calling create_all() in your code, call manually in the flask shell which is CLI
        Go to your terminal
        type `flask shell`, then
        `db.create_all()`

    Second method
        As it says in the runtime error message
        This typically means that you attempted to use functionality that needed the current application. To solve this, set up an application context with app.app_context().

        Open the python terminal in your project directory and manually add a context

        `from project_name import app, db`
        `app.app_context().push()`
        `db.create_all()`
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from dotenv import load_dotenv
import os
load_dotenv()




app_flask = Flask(__name__ , static_url_path='/static')
app_flask.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app_flask.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db = SQLAlchemy(app_flask)
bcrypt = Bcrypt(app_flask)
login_manager = LoginManager(app_flask)


from log import routes
