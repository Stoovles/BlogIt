from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from decouple import config
import os

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

# def create_production_app():
#     app = Flask(__name__)
#     app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///development.db?check_same_thread=False'
#     app.config['SECRET_KEY'] = os.urandom(16)
#     # Dynamically bind SQLAlchemy to application
#     db.init_app(app)
#     app.app_context().push()
#
#     from blogit import routes
#     return app


# def create_test_app():
#     app = Flask(__name__)
#     app.config['TESTING'] = True
#     app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db?check_same_thread=False'
#     app.config['SECRET_KEY'] = os.urandom(16)
#     # Dynamically bind SQLAlchemy to application
#     db.init_app(app)
#     app.app_context().push()  # this does the binding
#
#     from blogit import routes
#     return app


def create_test_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        TESTING=True,
        # a default secret that should be overridden by instance config
        SECRET_KEY=os.urandom(16),
        # store the database in the instance folder
        SQLALCHEMY_DATABASE_URI='sqlite:///test.db?check_same_thread=False',
    )
    app.app_context().push()  # this does the binding

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile("config.py", silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    # initialize plugins
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    login_manager.login_message_category = 'info'
    bcrypt.init_app(app)

    # apply the blueprints to the app
    from blogit import routes

    # register blueprint
    app.register_blueprint(routes.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app

def create_development_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY=os.urandom(16),
        # store the database in the instance folder
        # SQLALCHEMY_DATABASE_URI='postgres://meiadzikougoxp:63caa9d0a61d0064905a33e77dd535e704e00feae98a2b52a3941175c171d0c1@ec2-52-7-39-178.compute-1.amazonaws.com:5432/d1ratpbl9cvqhj',
        SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL'),

    )
    app.app_context().push()  # this does the binding

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile("config.py", silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    # initialize plugins
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    login_manager.login_message_category = 'info'
    bcrypt.init_app(app)
    migrate = Migrate(app, db)

    # apply the blueprints to the app
    from blogit import routes

    # register blueprint
    app.register_blueprint(routes.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    return app



