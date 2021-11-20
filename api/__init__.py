import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv

load_dotenv()

app = Flask( __name__ )
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = os.getenv('DB_URI')

db = SQLAlchemy( app )
