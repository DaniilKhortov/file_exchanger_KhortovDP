from .models import Account, db


def getLastId():

    last_entry = db.session.query(Account).order_by(Account.id.desc()).first()
    if last_entry:
        return last_entry.id 
    else:
        return None

def generateId(id):
    if id != None:
        return id+1
    else:
        return 0


 