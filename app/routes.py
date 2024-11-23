from flask import Blueprint, render_template, request, redirect, url_for, flash, make_response
from .models import Account, db
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from .utils import getLastId, generateId
main = Blueprint('main', __name__)
    
  
@main.route("/")
def home():
    return render_template("index.html")

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form['email']
        password = request.form['psw']
        existing_user = Account.query.filter_by(login=login, password=password).first()

        if existing_user.role=="admin":
            flash('Authorisation as Admin is successful!', 'success')
            response = make_response(redirect(url_for('main.admin'))) 
            response.set_cookie('authenticated', 'true', max_age=3600)  
            response.set_cookie('username', existing_user.login, max_age=3600) 
            return response 
        elif existing_user:
            flash('Authorisation is successful!', 'success')
            response = make_response(redirect(url_for('main.home')))
            response.set_cookie('authenticated', 'true', max_age=3600)  
            response.set_cookie('username', existing_user.login, max_age=3600) 
            return response 
        else:
            flash('User doesn`t exist in database!', 'fail')
        
        
        if existing_user.role=="admin":
            return redirect(url_for('admin.html')) 
        else:
            return redirect(url_for('index.html'))    
       
    return render_template("login.html")   

@main.route("/logout")
def logout():
    

    response = make_response(redirect(url_for('main.home')))
    response.set_cookie('authenticated', '', max_age=0) 
    response.set_cookie('username', '', max_age=0)  
    return response


@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        login = request.form['email']
        password = request.form['psw']
        password_repeat = request.form['psw-repeat']


        if password != password_repeat:
            flash('Passwords do not match!', 'fail')
            return redirect(url_for('main.register'))


        existing_user = Account.query.filter_by(login=login).first()
        
        if existing_user:
            flash('Login is already exists in database!', 'fail')
            return redirect(url_for('main.register'))

        userId = generateId(getLastId())
        print(userId)
        new_user = Account(id=userId, login=login, password=password, role="user")


        db.session.add(new_user)

        db.session.commit()

        flash('Account created successfully!', 'success')
        user = new_user
        
        return redirect(url_for('main.login'))  

    return render_template("register.html")
    
@main.route("/admin")
def admin():
    return render_template("admin.html")
        