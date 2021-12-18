from datetime import datetime
from project_flask import db


class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    image=db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(20),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)
 
    def __repr__(self):
        return f' {self.username}: {self.email}: {self.date_created}'
    

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    marks = db.Column(db.String(100), nullable=False)
 
 
    def __repr__(self):
        return f' {self.name}: {self.subject}: {self.marks}'   
        