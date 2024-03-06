from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
#from flask_jwt_extended import JWTExtended

app = Flask(__name__)

config = Config()

app.config['SECRET_KEY'] = config.api_key
app.config['SQLALCHEMY_DATABASE_URI'] = config.database_url

#jwt  = JWTExtended(app)

db = SQLAlchemy(app)

from app import routes_autor,routes_postagem