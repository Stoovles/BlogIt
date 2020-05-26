from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from dotenv import load_dotenv
import dotenv
import os

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_test_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    dotenv.load_dotenv()
    app.config.from_mapping(
        TESTING=True,
        # a default secret that should be overridden by instance config
        SECRET_KEY=os.urandom(16),
        # store the database in the instance folder
        SQLALCHEMY_DATABASE_URI='sqlite:///test.db?check_same_thread=False',
    )
    app.app_context().push()  # this does the binding

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return os.getenv('DATABASE_URL')

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
    # app.add_url_rule("/", endpoint="index")

    return app

def create_development_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    load_dotenv()
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY=os.urandom(16),
        # store the database in the instance folder
        SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL'),

    )
    app.app_context().push()  # this does the binding

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



