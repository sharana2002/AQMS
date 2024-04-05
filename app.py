# save this as app.py
from flask import Flask, request, render_template



import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('C:/Users/ACER/Desktop/AQMS/AQMS/knn_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method ==  'POST':
        PM2 = float(request.form[' PM'])
        PM10 = float(request.form[' PM10'])
        
        NO = float(request.form[' NO'])
        NO2= float(request.form[' NO2'])
        CO = float(request.form[' CO'])
        SO2= float(request.form[' SO2'])
        O3 = float(request.form['O3 '])
        AQI = float(request.form['AQI'])
        
        

        

       



        prediction = model.predict([[PM2,PM10,NO,NO2,CO,SO2,O3,AQI ]])

        # print(prediction)

        if(prediction=="Moderate"):
            prediction="Moderate"
        elif(prediction=="Poor"):
            prediction="Poor"
        elif(prediction=="Very Poor"):
             prediction="Very Poor"
        elif(prediction=="Satisfactory"):
             prediction="Satisfactory"
        elif(prediction=="Good"):
             prediction="Good"
        else :
            prediction="Severe"

        


        return render_template("prediction.html", prediction_text="Quality of Air is {}".format(prediction))




    else:
        return render_template("predict.html")



if __name__ == "__main__":
    app.run(debug=True)