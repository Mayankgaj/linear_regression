import pickle, bz2
from flask import Flask, request, render_template
import numpy as np
from logger import log

app = Flask(__name__)

# Import Regression model file
log.debug("Loading Model")
pickle_in = bz2.BZ2File('linear_regression.pkl', 'rb')
model_R = pickle.load(pickle_in)
log.debug("Successfully Model Loaded")


@app.route('/')
def home():
    log.debug('Home page loaded successfully')
    return render_template('boston_housing.html')


@app.route("/predict", methods=['POST'])
def predict():
    try:
        for x in request.form.values():
            if type(x) == str() or x == "":
                log.error('Input is Empty ,Give proper Input')
                return render_template('boston_housing.html', prediction_text1="Check the Input again!!!")
            else:
                data = [float(x) for x in request.form.values()]
                log.debug("Resizing data into 2D array")
                final_features = [np.array(data)]
                log.debug("Data in proper Shape ")
                output = model_R.predict(final_features)
                log.debug('Prediction done for Regression model')
                return render_template('boston_housing.html', prediction_text1="{}".format(output))
    except Exception as e:
        log.error('Input error, check input', e)
        return render_template('boston_housing.html', prediction_text2="Check the Input again!!!")


# Run APP in Debug mode
if __name__ == "__main__":
    app.run(debug=True, port=2525)
