from flask import Blueprint, render_template, request, redirect, url_for, flash, make_response, jsonify, send_file
from .models import Account, File, Log, db
from .utils import getLastId, generateId, checkRegisterFiles, checkFileRecords, deleteFile
from . import basedir
import os
from datetime import datetime
from sqlalchemy import func
main = Blueprint('main', __name__)
  
@main.route("/")
def home():
    login = request.cookies.get('username')
    existing_user = Account.query.filter_by(login=login).first()
    filesDB = File.query.all()
    try:
        if existing_user.role =="admin":
            filesTable = File.query.all()
            logsTable = Log.query.order_by(Log.id.desc()).all()

            activityTable = (
                db.session.query(
                    Account.login.label('username'),
                    func.count(Log.id).label('downloads'),
                    func.max(Log.time).label('lastActivity'),

                )
                .join(Log, Account.login == Log.login)

                .group_by(Account.login)
                .order_by(func.count(Log.id).desc())
                .all()
                )
            return render_template("admin.html", files=filesTable, logs = logsTable, activity=activityTable)
        else:

            return render_template("index.html", files=filesDB)
    except AttributeError:

        return render_template("index.html", files=filesDB)


@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form['email']
        password = request.form['psw']
        existing_user = Account.query.filter_by(login=login, password=password).first()
        if existing_user:
            
            if existing_user.role=="admin":
                flash('Authorisation as Admin is successful!', 'success')
                response = make_response(redirect(url_for('main.admin'))) 
                response.set_cookie('authenticated', 'true', max_age=3600)  
                response.set_cookie('username', existing_user.login, max_age=3600) 
                return response 
            else:
                flash('Authorisation is successful!', 'success')
                response = make_response(redirect(url_for('main.home')))
                response.set_cookie('authenticated', 'true', max_age=3600)  
                response.set_cookie('username', existing_user.login, max_age=3600) 
                return response 
        
        if existing_user:
            if existing_user.role=="admin":
                return redirect(url_for('admin.html')) 
            else:
                return redirect(url_for('index.html'))    
        else:
            flash('User doesn`t exist in database!', 'fail')  
       
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

        userId = generateId(getLastId(Account))
        print(userId)
        new_user = Account(id=userId, login=login, password=password, role="user")


        db.session.add(new_user)

        db.session.commit()

        flash('Account created successfully!', 'success')
        user = new_user
        
        return redirect(url_for('main.login'))  

    return render_template("register.html")
 
 
@main.route("/upload", methods=['POST'])
def upload():
    if "file" not in request.files:
        return "No file part", 400
    
    file = request.files['file']
    if file.filename == '':
        flash('Failed to upload file!', 'fail')
        return redirect(url_for('main.admin')) 


    file.save(f"./app/storage/{file.filename}")
    checkRegisterFiles()
    checkFileRecords()
    
    flash('File was successfully uploaded!', 'success')
    return redirect(url_for('main.admin'))  
        
@main.route("/admin")
def admin():
    filesTable = File.query.all()
    logsTable = Log.query.order_by(Log.id.desc()).all()

    activityTable = (
        db.session.query(
            Account.login.label('username'),
            func.count(Log.id).label('downloads'),
            func.max(Log.time).label('lastActivity'),

        )
        .join(Log, Account.login == Log.login)

        .group_by(Account.login)
        .order_by(func.count(Log.id).desc())
        .all()
    )
    return render_template("admin.html", files=filesTable, logs = logsTable, activity=activityTable)
        
        
@main.route("/updateRecordStatus", methods=['POST'])   
def updateRecordStatus():
    data = request.get_json()
    if not data or 'id' not in data or 'display' not in data:
        return jsonify({'error': 'No JSON received'}), 400   
    
    recordId = data['id']
    displayStatus = data['display']  
    file = File.query.filter_by(id=recordId).first()
    file.display=str(displayStatus)
    try:

        db.session.commit()
        return {"success": f"Field updated successfully for file with ID {recordId}"}
    except Exception as e:
        checkRegisterFiles()
        checkFileRecords()
        db.session.rollback()
        return {"error": f"Failed to update field: {str(e)}"}
    
@main.route("/download", methods=['POST'])   
def download():
    data = request.get_json()
    if not data or 'id' not in data:
        return jsonify({'error': 'No JSON received'}), 400   
    
    fileId = data['id']
    userName = data['accountName']
    file = File.query.filter_by(id=fileId).first()
    try:
        
        path = os.path.join(basedir, "storage")
        path = os.path.join(path, file.name)
        
        if os.path.isfile(path):
            
            response = send_file(path, as_attachment=True, download_name=file.name)
            

            response.headers['File-Name'] = file.name
            
            file.downloads+=1
            db.session.commit()
            logId = generateId(getLastId(Log))

            currentTime = datetime.now().strftime("%d-%m-%Y %H:%M")

            newLog= Log(id=logId, login=userName, file=file.name, time=currentTime)
            db.session.add(newLog)

            db.session.commit()


            return response
        else:
            raise Exception("File was removed from server!")
    except Exception as e:
        checkRegisterFiles()
        checkFileRecords()
        db.session.rollback()
        return jsonify({"error": f"Failed to download file: {str(e)}"}), 500  
    
@main.route("/delete", methods=['POST'])
def delete():
    data = request.get_json()
    if not data or 'id' not in data:
        return jsonify({'error': 'No JSON received'}), 400   
    
    fileId = data['id']
    targetFile = File.query.filter_by(id=fileId).first()
    
    if targetFile:
        deleteFile(targetFile.name) 
        checkRegisterFiles()  
        checkFileRecords() 
        flash('File was successfully deleted!', 'success')
    
    return jsonify({'status': 'success'})

       