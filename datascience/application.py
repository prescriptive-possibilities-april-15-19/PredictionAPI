#!flask/bin/python
import json
import pickle
from flask import Flask, Response
from datascience.flaskrun import flaskrun


application = Flask(__name__, static_folder=None)

with open("models/predict.pickle", "rb") as fp:
    predict = pickle.load(fp)

@application.route("/predict", methods=["POST"])
def predict():
    smiles = request.form.get('smiles')
    pr_seq = request.form.get('sequence')
    if smiles != "" and pr_seq != "":
        return str(predict.predict(data_lig, data_seq))
    return str(-1.0)

if __name__ == '__main__':
    flaskrun(application)
