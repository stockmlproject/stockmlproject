import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__) #Create app

#Load models
close = 'modelo_cierre.sav'
close_model = pickle.load(open(close, 'rb'))

high = 'modelo_high.sav'
high_model = pickle.load(open(high, 'rb'))

# Bind home function to URL
@app.route('/')
def home():
    return render_template('index.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])

def close_predict():
 
    # Put all form entries values in a list
    opn = request.form.get("open")
    hgh = request.form.get("high")
    low = request.form.get("low")

    prch = request.form.get("price")
    opnh = request.form.get("openh")
    lowh = request.form.get("lowh")

    if(opn != None and hgh != None and low != None ):
        try:
            features = [float(i) for i in request.form.values()]
            # Convert features to array
            array_features = [np.array(features)]
            # Predict features
            prediction = close_model.predict(array_features)
 
            output = prediction
            return render_template('index.html', resultclose = output)
       
        except:
            return render_template('index.html', resultclose = "Invalid input")

    elif(prch != None and opnh != None and lowh != None ):
        try:        
            features = [float(i) for i in request.form.values()]
            # Convert features to array
            array_features = [np.array(features)]
            # Predict features
            prediction = high_model.predict(array_features)
 
            output = prediction
            return render_template('index.html', resulthigh = output)
       
        except:
            return render_template('index.html', resulthigh = "Invalid input")
   
    return render_template('index.html', result = "Invalid input")

if __name__ == '__main__':
    #Run the application
    app.run()
