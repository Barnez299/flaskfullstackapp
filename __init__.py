from flask import Flask
from flask_sqlalchemy import SQLAlchemy





def create_app():
    app = Flask(__name__)


    # register main blueprint

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # register auth blueprint

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    return app