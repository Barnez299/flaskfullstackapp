from flask import Flask
from flask_sqlalchemy import SQLAlchemy







def create_app():
    app = Flask(__name__)

    # set up db instance
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456789@localhost:5432/user'

    db = SQLAlchemy(app)
    db.init_app(app)


    # register main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # register auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    return app