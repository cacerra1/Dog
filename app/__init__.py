# app/__init__.py
import os
from flask import Flask, request, render_template_string
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt  # this is for bcrypt hashing  # see below
from flask_heroku import Heroku
from flask_migrate import Migrate, Manager,  MigrateCommand


db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_the_login' # this lets the login_manager know about the login route we are using to log the user into the application
login_manager.session_protection = 'strong'  # protects the user session. force user to logout and log back in
bcrypt = Bcrypt()
heroku = Heroku()


def create_app(config_type):  # dev, test, or prod

    app = Flask(__name__)
    #configuration = "/Users/claudiaacerra/PycharmProjects/Dogs/config/dev.py"
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_object(configuration)


    app.config.from_pyfile(configuration)
    db.init_app(app)  # initialize database
    #babel = Babel(app)

    bootstrap.init_app(app)  # initialize bootstrap
    login_manager.init_app(app)  # initialize login_manager
    bcrypt.init_app(app)
    migrate = Migrate(app, db)
    heroku.init_app(app)


    #UserManager.init_app(app, db, User)
    #user_manager = UserManager(app, db, User)
    #the_password = 'Admin1'
    #hashed_password = user_manager.hash_password(the_password)






    from app.dogs.models import Dog, Purchase, Store, Vet, VetVisit, Doctor  # this is KEY.. without this I will not be able to create the table
    from app.auth.models import User
    from app.dogs import main
    app.register_blueprint(main)

    from app.auth import authentication
    app.register_blueprint(authentication)





    return app