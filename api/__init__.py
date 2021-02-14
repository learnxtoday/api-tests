from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from .views import main

def create_app():
    app = Flask(__name__)

    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'this-too-shall-pass'


    app.register_blueprint(main, url_prefix='')

    app.run(port=3000)

