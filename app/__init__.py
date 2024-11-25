from flask import Flask
import os

from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

def file_exchanger_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'adminConfig'

    app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'accountsData.db')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
    
    db.init_app(app)
    
    from .routes import main
    app.register_blueprint(main)

    return app