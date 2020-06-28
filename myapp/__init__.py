from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '49$5fHG@_CB12af34'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .todo import todo as todo_blueprint
    app.register_blueprint(todo_blueprint)

    return app