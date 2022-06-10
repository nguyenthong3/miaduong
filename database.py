from datetime import datetime
from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Paradigm(db.Model):
    __tablename__ = 'paradigm'
    id=db.column(db.Integer, primary_key=True)
    name=db.column(db.String(40),unique=True)
    result = db.relationship('Result',backref="models")

    def __init__(self,name,result):
        self.name = name
        self.result = result

class StoreFile(db.Model):
    __tablname__ = 'store_file'
    id=db.column(db.Integer, primary_key=True)
    filename=db.collumn(db.String(30))
    id_result=db.column(db.Integer)

class Result(db.Model):
    __tablename__ = 'result'
    id=db.column(db.Integer, primary_key=True)
    created_at=db.column(db.DateTime, default=datetime.utcnow)
    id_model=db.column(db.Integer,db.Foreignkey('Models.id'))
    predict_result=db.column(db.Float)
    # def __init__*(self, **kwargs):
    #     super().__intin__()

