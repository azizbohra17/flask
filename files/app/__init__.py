from flask import Flask
from flask_sqlalchemy import SQLAlchemy  
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = '1b397cb3e7647fca6a2c87e0ef579aae'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

login_manager = LoginManager(app)
login_manager.login_view= 'login'
login_manager.login_message_category= 'info'

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from app import routes 