from . import db

class Account(db.Model):
    __tablename__ = 'ACCOUNT'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(320), nullable=False)
    password = db.Column(db.String(320), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    def __repr__(self):
        return f'<Account {self.login}>'
