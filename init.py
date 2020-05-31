import numpy as np
from flask import Flask, request, render_template, url_for
import pickle
import joblib

app = Flask(__name__)
model = joblib.load("/Users/tushararora/Documents/IPL Prediction/IPL prediciton.pkl")
#------For testing purpose
# predictions = model.predict([['1','2','4','1','0']])
# team = ''
# if predictions[0] == 1:
#     team = 'MI'
# elif predictions[0] == 2:
#     team = 'KKR'
# elif predictions[0] == 3:
#      team = 'RCB'
# elif predictions[0] == 4:
#      team = 'DC'
# elif predictions[0] == 5:
#     team = 'CSK'
# elif predictions[0] == 6:
#     team = 'RR'
# elif predictions[0] == 7:
#     team = 'DD'
# elif predictions[0] == 8:
#     team = 'GL'
# elif predictions[0] == 9:
#     team = 'KXIP'
# elif predictions[0] == 10:
#     team = 'SRH'
# elif predictions[0] == 11:
#     team = 'RPS'
# elif predictions[0] == 12:
#     team = 'KTK'
# elif predictions[0] == 12:
#     team = 'PW'
# else:
#     team = "Draw"
# print(team)
#--------------------------#
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    input_features = [str(x) for x in request.form.values()]
    value = np.array(input_features)
    predictions = model.predict([value])
    print(predictions)
    team = ''
    if predictions[0] == 1:
        team = 'MI'
    elif predictions[0] == 2:
        team = 'KKR'
    elif predictions[0] == 3:
        team = 'RCB'
    elif predictions[0] == 4:
        team = 'DC'
    elif predictions[0] == 5:
        team = 'CSK'
    elif predictions[0] == 6:
        team = 'RR'
    elif predictions[0] == 7:
        team = 'DD'
    elif predictions[0] == 8:
        team = 'GL'
    elif predictions[0] == 9:
        team = 'KXIP'
    elif predictions[0] == 10:
        team = 'SRH'
    elif predictions[0] == 11:
        team = 'RPS'
    elif predictions[0] == 12:
        team = 'KTK'
    else:
        team = 'PW'
    print(team)
    return render_template('index.html', Prediction_text = f"According to the prediction the {team} Wins\'prediction is high")
if __name__ == "__main__":
    app.run(debug=True)