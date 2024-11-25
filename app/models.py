from . import db

class Account(db.Model):
    __tablename__ = 'ACCOUNT'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(320), nullable=False)
    password = db.Column(db.String(320), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    def __repr__(self):
        return f'<Account {self.login}>'

class File(db.Model):
    __tablename__ = 'FILE'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    display = db.Column(db.String(10), nullable=False)
    downloads = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return (f'<File {self.name}>')
    
class Log(db.Model):
    __tablename__ = 'LOG'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(320), nullable=False)
    file = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return (f'<Log {self.id}>')    