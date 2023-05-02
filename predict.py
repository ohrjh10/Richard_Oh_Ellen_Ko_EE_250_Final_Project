import pickle
from flask import Flask,request
import json

clf = pickle.load(open('model.pickle','rb'))


app = Flask(__name__)

@app.route("/classify")
def hello_world():
    temperature = float(request.args.get('w'))
    humidity = float(request.args.get('r'))

    label = int(clf.predict([[temperature, humidity]])[0])
    #print(label)
    return json.dumps({"temperature":temperature, "humidity":humidity ,"label":label})
