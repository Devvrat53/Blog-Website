from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '4f73487168a9c36e5384f13525a0a01b'
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite.///site.db' # site.db will be created in the same directory in which we are working!
# With SQLAlchemy, we can store databases as classes
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# to avoid circular calling error
from flaskblog import routes