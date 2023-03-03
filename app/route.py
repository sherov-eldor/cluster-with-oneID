from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/auth/register')
def register():
    return render_template('auth/register.html')

@app.route('/auth/login')
def login():
    return render_template('auth/login.html')