import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PWD = os.getenv("MYSQL_PWD", "test")
MYSQL_DB = os.getenv("MYSQL_DB", "myblog_db")

app = Flask(__name__, 
            template_folder="../templates",
            static_folder="../assets",
            static_url_path="/assets")

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_PWD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
app.config['SECRET_KEY'] = 'ac9802rgr8c789az1019594d'

db = SQLAlchemy(app)
login_manager = LoginManager(app) 

from routes import user_route 
from routes import admin_route 
