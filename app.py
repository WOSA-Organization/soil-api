from flask import Flask, render_template, redirect, url_for, Response, request, session
import pandas as pd
import plotly.graph_objects as go
import requests
import json
import plotly
import plotly.express as px


app = Flask(__name__,template_folder='templates')
# ROUTES
@app.route('/')
def home():
    return render_template('main_s.html')

@app.route("/success", methods=["GET", "POST"])
def soil():
    lat = request.form['lat']
    lng = request.form['long']
    url = "https://api.ambeedata.com/soil/latest/by-lat-lng"
    querystring = {"lat":lat,"lng":lng}
    headers = {
        'x-api-key': "45bc722a000629ee4bb92e0158710002d1c69cafa0b199e6f262a6ad46b4d9d0",
        'Content-type': "application/json"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response.text)
    r = response.json()
    lab = r.get("data")
    temp = list(lab[0].values())
    values = temp[1:]
    print(type(values))
    stemp = values[0]
    smoist = values[1]
    return render_template("success_s.html", stemp = stemp, smoist = smoist)
if __name__ == "__main__":
    app.run(debug=True)
