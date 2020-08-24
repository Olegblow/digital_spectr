import os
from dotenv import load_dotenv
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


load_dotenv()
app = Flask(__name__)

# todo вынести в conf
DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASS = os.getenv('POSTGRES_PASSWORD')
PG_HOST = os.getenv('PG_HOST')

DB_URI = f'postgres://{DB_USER}:{DB_PASS}@{PG_HOST}:5432/{DB_NAME}'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)


from app import models, routes
