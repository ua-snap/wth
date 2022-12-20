from flask import Flask
import json

app = Flask(__name__)


polys = open("../data/t2.json")
jj = json.load(polys)
print(jj)

@app.route("/")
def hello_world():
    return jj