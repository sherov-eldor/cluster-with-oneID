from app import app, oneid, db, login_manager
from flask import render_template, request, redirect, url_for, jsonify
from flask_login import current_user, login_user, login_required, logout_user

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

@login_manager.user_loader
def load_user(user_id):
    if user_id != "None":
        return User.query.get(int(user_id))
    else :
        pass
        

@app.route('/get/params', methods = ['GET'])
def get_params():
    data = oneid.Params_To_Dict(request.args)
    user_req = User.query.filter_by(user_id = data['user_id']).first()
    if user_req : 
        login_user(user_req)
    else :  
        user = User(pin = data['pin'], full_name = data['full_name'], email = data['email'], user_id = data['user_id'], pport_no = data['pport_no'])
        db.session.add(user)
        db.session.commit()
        login_user(user)
    return redirect('/')

@app.route('/user/profile')
@login_required
def user_profile():
    return render_template('profile.html')

@app.route('/user/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))