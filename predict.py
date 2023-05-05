import pickle
from flask import Flask,request
import json

clf = pickle.load(open('model.pickle','rb'))


app = Flask(__name__)

@app.route("/classify")
def hello_world():
    humidity = float(request.args.get('w'))
    pressure = float(request.args.get('r'))

    clearness = int(clf.predict([[humidity,pressure]])[0])
    #print(clearness)
    return json.dumps({"humidity":humidity, "pressure":pressure ,"clearness":clearness})
