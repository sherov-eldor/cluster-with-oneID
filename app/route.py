from app import app, oneid, db
from flask import render_template, request, redirect, url_for, jsonify

from app.models import User

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/auth/register')
def register():
    return render_template('auth/register.html')

@app.route('/auth/login')
def login():
    return render_template('auth/login.html')

@app.route('/get/params', methods = ['GET'])
def get_params():
    data = oneid.Params_To_Dict(request.args)
    user = User(pin = data['pin'], full_name = data['full_name'], email = data['email'], user_id = data['user_id'], pport_no = data['pport_no'])
    db.session.add(user)
    db.session.commit()
    return jsonify(data)