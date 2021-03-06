# -*- coding: utf-8 -*-


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('Final_model_xg.pkl', 'rb'))

@app.route("/",methods=['GET'])

def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0], 2)
    if output == 0:
        return render_template('result_no_rain.html')
    else:
        return render_template('result_rain.html')
    return render_template('temp.html', prediction_text='rain tomorrow??? {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
