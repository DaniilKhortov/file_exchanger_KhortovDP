from .models import Account, File, Log, db
from datetime import date
import os
from . import basedir

def getLastId(table):

    last_entry = db.session.query(table).order_by(table.id.desc()).first()
    if last_entry:
        return last_entry.id 
    else:
        return None

def generateId(id):
    if id != None:
        return id+1
    else:
        return 0

def checkRegisterFiles():
    storageDir = os.path.join(basedir, "storage")
    filesInDirectory = set(os.listdir(storageDir))
    for file in filesInDirectory:
        fileRecord = db.session.query(File.name).filter(File.name==file).first()
        
        if fileRecord is None:
            newId = generateId(getLastId(File))
            newSize = os.path.getsize(os.path.join(storageDir, file))
            sizeType="b"
            if newSize/1024>1:
                newSize=round(float(newSize/1024), 1)
                sizeType="KB"
            if newSize/1024>1:
                newSize=round(float(newSize/1024), 1)
                sizeType="MB"                
            if newSize/1024>1:
                newSize=round(float(newSize/1024), 1)
                sizeType="GB"                  
            
            currentDate = date.today().strftime("%d-%m-%Y")
            newFile = File(id=newId, name=file, size=str(str(newSize)+" "+ sizeType), date=currentDate, display="True", downloads=0)
            db.session.add(newFile)
            db.session.commit()
 
def checkFileRecords():
    storageDir = os.path.join(basedir, "storage")
    filesInDirectory = set(os.listdir(storageDir))
    
    filesInDatabase = db.session.query(File).all()
    for fileRecord in filesInDatabase:
        if fileRecord.name not in filesInDirectory:
            db.session.delete(fileRecord) 
            db.session.commit()

def deleteFile(name):
    storageDir = os.path.join(basedir, "storage")   
    targetFile = os.path.join(storageDir, name)   
    os.remove(targetFile)
