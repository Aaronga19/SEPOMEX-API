from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sepomex import routes
from sepomex.config import settings
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
app.config['SECRET_KEY'] = settings.secret_key
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'