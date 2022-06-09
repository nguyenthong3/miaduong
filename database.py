from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Models(db.Model):
    id=db.column(db.Integer, primary_key=True)
    name=db.column(db.String,)
    result = db.relationship('Result',backref="models")

    def __repr__(self) -> str:
        return 'name>>>{self.name}'

class StoreFile(db.Model):
    id=db.column(db.Integer, primary_key=True)
    filename=db.collumn(db.String(30))
    id_result=db.column(db.Integer)

class Result(db.Model):
    id=db.column(db.Integer, primary_key=True)
    created_at=db.column(db.DateTime, default=datetime.now())
    id_model=db.column(db.Integer,db.Foreignkey('Models.id'))
    predict_result=db.column(db.Float)
    # def __init__*(self, **kwargs):
    #     super().__intin__()

