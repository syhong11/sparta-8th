from flask import Flask, render_template, request, jsonify

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://test:test@localhost', 27017)   
# db = client.schoolzonedb
db = client.schoolzoneDB

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('school.html')

@app.route('/api/list')
def points_retreive():
    region_receive = request.args.get('region_give')

    points = list(db.school.find({'Agency': { '$regex' : region_receive, '$options' : 'i' }}, {'_id': False, 'Latitude': True, 'Longitude': True}))

    return jsonify({
        'result': 'success',
        'school': points
    })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)