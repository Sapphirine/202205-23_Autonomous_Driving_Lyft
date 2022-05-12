from flask import Flask, redirect, render_template
from threading import Thread
application = Flask(__name__, static_folder='assets')
@application.route("/")
def Home():
    return render_template('index.html')

@application.route("/index.html")
def BackHome():
    return render_template('index.html')

@application.route('/Dataset.html')
def loadData():
    return render_template('Dataset.html')

@application.route('/Methodology.html')
def loadMethod():
    return render_template('Methodology.html')  

@application.route('/Visualized Prediction.html')
def loadPrediction():
    return render_template('Visualized Prediction.html')  

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True, threaded=True)