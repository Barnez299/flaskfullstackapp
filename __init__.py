from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()




def create_app():
    app = Flask(__name__)

    # set up db instance
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456789@localhost:5432/user'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['debug'] = True

    db = SQLAlchemy(app)

    db.init_app(app)

    # set up login manager

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    # register main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # register auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    return app