from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()

# def create_production_app(config=None):
#     """Construct the core application."""
#     app = Flask(__name__, instance_relative_config=True)
#     db.init_app(app)
#     if config is None:
#         app.config.from_object(config.BaseConfig)
#     else:
#         app.config.from_object(config)
#
#     with app.app_context():
#         # Imports
#         from . import routes
#         db.create_all()
#
#         return app
def create_production_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///development.db?check_same_thread=False'
    # Dynamically bind SQLAlchemy to application
    db.init_app(app)
    app.app_context().push()
    return app

def create_test_app():
    app = Flask(__name__)
    app.config['TESTING'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db?check_same_thread=False'
    # Dynamically bind SQLAlchemy to application
    db.init_app(app)
    app.app_context().push() # this does the binding
    return app
# app = Flask(__name__)
# SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db?check_same_thread=False'
# db = SQLAlchemy(app)
bcrypt = Bcrypt(app=create_production_app())
login_manager = LoginManager(app=create_production_app())
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# from blogit import routes
