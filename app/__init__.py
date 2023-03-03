from flask import Flask
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config['SECRET_KEY'] = '114d7b45bc27a059cfb5f327378eb01d'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/contours_by_id'

# db = SQLAlchemy(app)

from app import route