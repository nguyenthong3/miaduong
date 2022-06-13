import datetime
from importlib.metadata import files
import os
# from flask_sqlalchemy import SQLAlchemy

import numpy as np
import appdo
import time

from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_restful import Api
from werkzeug.utils import secure_filename

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config["CSV_UPLOADS"] = 'static/files'
app.config["ALOWED_EXSTENSION"] = ["CSV"]


# db=SQLAlchemy(app)

# class Models(db.Model):
#     id=db.column(db.Integer, primary_key=True)
#     name=db.column(db.String,)
#     result = db.relationship('Result',backref="models")

#     def __repr__(self) -> str:
#         return 'name>>>{self.name}'

# class StoreFile(db.Model):
#     id=db.column(db.Integer, primary_key=True)
#     filename=db.collumn(db.String(30))
#     id_result=db.column(db.Integer)

# class Result(db.Model):
#     id=db.column(db.Integer, primary_key=True)
#     created_at=db.column(db.DateTime, default=datetime.now())
#     id_model=db.column(db.Integer,db.Foreignkey('Models.id'))
#     predict_result=db.column(db.Float)

def allowed_file(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALOWED_EXSTENSION"]:
        return True
    else:
        return False

@app.route("/")
@app.route("/homepage")
def ToHomePage():
    return render_template("index.html")


@app.route("/do/<criteria>", methods=['POST'])
def calculated(criteria):

    if request.files:

        file = request.files["csv"]

        if file.filename == "":
            print("csv must have a filename!")
            return jsonify({'error': 'Missing file!'})

        if not allowed_file(file.filename):
            print("That is not allowed")
            return jsonify({'error': 'That is not a csv file!'})
        else:
            ml = int(time.time() * 1000)
            filename = secure_filename(str(ml) + file.filename)
            file.save(os.path.join(app.config["CSV_UPLOADS"], filename))
            print("File Saved")
            if criteria == "brix":
                res = appdo.doAll(filename,criteria)
                lr = "Linear Regression"
                svr = "Support Vector Regression"
                rf = "Random Forest"
                res1 = res.get('LR')
                res2 = res.get('SVR')
                res3 = res.get('RF')
                return render_template("result.html",criteria = "Kết quả phân tích bằng tiêu chí Brix",name1 = lr,name2 = svr, name3 = rf , result1 = res1, result2= res2, result3= res3)
            if criteria == "nguongoc":
                ldaName = "Linear Discriminant Analysis"
                svmName = "Support Vector Machine"
                rfName = "Random Forest"
                res = appdo.doAll(filename,criteria)
                lda = res.get('LDA')
                svr = res.get('SVM')
                rf = res.get('RF')
                return render_template("result.html",criteria = "Kết quả truy xuất Nguồn gốc",name1 = ldaName,name2 = svmName, name3 = rfName,result1 = lda, result2 = svr, result3 = rf)
            if criteria == "doam":
                res = appdo.doAll(filename,criteria)
                lda = res.get('LDA')
                svr = res.get('SVR')
                rf = res.get('RF')
                return render_template("result.html",criteria = "Kết quả phân tích bằng tiêu chí Độ ẩm",result1 = lda, result2 = svr, result3 = rf)


@app.route("/dotest/<criteria>",methods=['POST'])
def dotest(criteria):
    if request.files:

        file = request.files["csv"]

        if file.filename == "":
            print("csv must have a filename!")
            return jsonify({'error': 'Missing file!'})

        if not allowed_file(file.filename):
            print("That is not allowed")
            return jsonify({'error': 'That is not a csv file!'})
        else:
            ml = int(time.time() * 1000)
            filename = secure_filename(str(ml) + file.filename)
            file.save(os.path.join(app.config["CSV_UPLOADS"], filename))
            print("File Saved")
            res = appdo.doAll(filename,criteria)
            return res



@app.route("/deletebb$Xs*B}Zr2Y6cX",methods=['POST'])
def deleteAllCSV():
    appdo.deleteAllFile()
    return jsonify({'status': 'OK'})


@app.route("/testne", methods=['POST'])
def updateDCM():
    random_decimal = np.random.rand()
    return jsonify('',render_template('test_add.html',x=random_decimal))

@app.route('/xxx')
def xxx():
    random_decimal = np.random.rand()
    return render_template('test.html',x=random_decimal)

if __name__ == "__main__":
    app.run(port=5000,debug=True)

# serve(app, host='0.0.0.0', port=5006, threads=1)