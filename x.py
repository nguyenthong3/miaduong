import numpy as np
import pandas as pd
import joblib
from scipy.signal import savgol_filter


def toPixels(pixels):
    arr = np.array(pixels.split(), "float64")
    arr = arr.reshape(228, )
    return arr


def readLRBrix(absorbance):
    filename = 'LRBrix.pkl'
    loaded_model = joblib.load('LRBrix.pkl')
    ln = loaded_model.predict(absorbance.reshape(1, 228))
    return float(ln)


def readSVRBrix(absorbance):
    filename = 'SVRBrix.pkl'
    loaded_model = joblib.load('SVRBrix.pkl')
    ln = loaded_model.predict(absorbance.reshape(1, 228))
    return float(ln)


def readRFBrix(absorbance):
    filename = 'RFBrix.pkl'
    loaded_model = joblib.load('RFBrix.pkl')
    ln = loaded_model.predict(absorbance.reshape(1, 228))
    return float(ln)


def readXXX():
    return 1


def doAll(filename):
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

    d = {"LR": readLRBrix(Absorbance), "SVR": readSVRBrix(Absorbance), "RF": readRFBrix(Absorbance)}

    return d
