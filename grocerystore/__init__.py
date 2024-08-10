from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path

db = SQLAlchemy()
db_name = "shoppingsite.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "ProjectHCI"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_name}"
    db.init_app(app)
    app.app_context().push()
    app.static_folder = "static"

    from .user import user
    app.register_blueprint(user, url_prefix = "/")

    from .auth import auth
    app.register_blueprint(auth, url_prefix = "/")
    
    from .models import User

    create_database(app)
     
    return app


def create_database(app):
    if not path.exists("instance/"+db_name):
        db.create_all()