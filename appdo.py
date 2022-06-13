import glob
import numpy as np
import pandas as pd
import joblib
import send2trash as s2t

from scipy.signal import savgol_filter


def toPixels(pixels):
    arr = np.array(pixels.split(), "float64")
    arr = arr.reshape(228, )
    return arr


def readLRBrix(absorbance):
    loaded_model = joblib.load('./pkdfile/LRBrix.pkl')
    ln = loaded_model.predict(absorbance.reshape(1, 228))
    return float(ln)


def readSVRBrix(absorbance):
    loaded_model = joblib.load('./pkdfile/SVRBrix.pkl')
    ln = loaded_model.predict(absorbance.reshape(1, 228))
    return float(ln)


def readRFBrix(absorbance):
    loaded_model = joblib.load('./pkdfile/RFBrix.pkl')
    ln = loaded_model.predict(absorbance.reshape(1, 228))
    return float(ln)

def readLDACFL(absorbance):
    class_dict = {"[1]": "Đường Lam Sơn", "[0]" : "Đường Biên Hòa","[2]":"Đường Hoàng Mai","[3]":"Đường TL"}
    loaded_model = joblib.load('./pkdfile/LDA_CFL.pkl')
    ln = loaded_model.predict(absorbance.reshape(1, 228))
    print(ln)
    return class_dict[str(ln)]

def readRFCFL(absorbance):
    class_dict = {"[1]": "Đường Lam Sơn", "[0]" : "Đường Biên Hòa","[2]":"Đường Hoàng Mai","[3]":"Đường TL"}
    loaded_model = joblib.load('./pkdfile/RF_CFL.pkl')
    ln = loaded_model.predict(absorbance.reshape(1, 228))
    print(ln)
    return class_dict[str(ln)]

def readSVMCFL(absorbance):
    class_dict = {"[1]": "Đường Lam Sơn", "[0]" : "Đường Biên Hòa","[2]":"Đường Hoàng Mai","[3]":"Đường TL"}
    loaded_model = joblib.load('./pkdfile/SVM_CFL.pkl')
    ln = loaded_model.predict(absorbance.reshape(1, 228))
    print(ln)
    return class_dict[str(ln)]


def doAll(filename,criteria):
    """**Principal Component Analysis**"""

    data_demo = pd.read_csv("./static/files/"+filename)
    input_demo = data_demo["Hadamard 1"][21:21 + 229]
    input_demo = np.array(input_demo.astype('float64'))
    input_dfeat = savgol_filter(input_demo, 25, polyorder=5, deriv=1)

    Absorbance = np.array(input_dfeat)
    data_mean = np.mean(Absorbance)
    data_std = np.std(Absorbance)
    one = np.ones_like(228, )
    Absorbance = (Absorbance - one * data_mean) / data_std

    if criteria == "brix":
        d = {"LR": readLRBrix(Absorbance), "SVR": readSVRBrix(Absorbance), "RF": readRFBrix(Absorbance)}
    if criteria == "doam":
        d = {"LR": 1, "SVR": 2, "RF": 3}
    if criteria == "nguongoc":
        d = {"LDA": readLDACFL(Absorbance), "SVM": readSVMCFL(Absorbance), "RF": readRFCFL(Absorbance)}
    
    return d

def deleteAllFile():
    target = glob.glob("./static/files/*")
    for x in target:
        s2t.send2trash(x)