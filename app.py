from asyncio import threads
from concurrent.futures import thread
import json
import os
import x
import time

from flask import Flask, render_template, redirect, request, url_for, jsonify
from flask_restful import Api
from werkzeug.utils import secure_filename
from waitress import serve

app = Flask(__name__)
api = Api(app)

app.config["CSV_UPLOADS"] = 'static/files'
app.config["ALOWED_EXSTENSION"] = ["CSV"]


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


@app.route("/do", methods=['POST'])
def calculated():
    if request.method == 'POST':
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
                res = x.doAll(filename)
                res1 = res.get('LR')
                res2 = res.get('SVR')
                res3 = res.get('RF')
                return render_template("result.html",result1 = res1, result2= res2, result3= res3)



if __name__ == "__main__":
    app.run()

serve(app, host='0.0.0.0', port=5000, threads=1)
