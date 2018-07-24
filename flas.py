from flask import Flask 
from flask import request
import sqlite3
import requests
import json
import req
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    con = sqlite3.connect('database.db')
    c = con.cursor()
    x = request.args.get('citi', default = '*', type = str)
    if x == "*":
        return "error citis missing"
    c.execute("SELECT * FROM stocks")
    url = 'https://geocoder.cit.api.here.com/6.2/geocode.json?app_id=LGKseBzhB368K4hkIZ7c&app_code=jj1R0tMgUUquGiZ6oe_h3Q&searchtext=' + x
    r = requests.get(url)
    a = r.json()
    if len(a['Response']['View']) == 0:
        return json.dumps({'response':[]},indent=2)
    c = a['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']
    b = a['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
    d = "Longitude" + str(c) + " & Latitude" + str(b)
    return req.output(b,c)
    
if __name__ == "__main__":
    app.run()