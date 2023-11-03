from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://wtsxwycy:EmqxAumxxNoYdhnqQFqvnDYjmaLD0QZu@trumpet.db.elephantsql.com/wtsxwycy'
db = SQLAlchemy(app)

from application import routes