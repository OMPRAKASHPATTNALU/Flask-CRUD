from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
  
app.config['SECRET_KEY']='newsecretkey'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/search.db'

db=SQLAlchemy(app)
from project_flask import routes