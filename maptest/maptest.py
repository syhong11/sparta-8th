from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('localhost', port=27017)
db = client.schoolzonedb

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('maptest.html')

@app.route('/api/list')
def points_retreive():
    region_receive = request.args.get('region_give')

    points = list(db.school.find({'Agency': { '$regex' : region_receive, '$options' : 'i' }}, {'_id': False, 'Latitude': True, 'Longitude': True}))

    return jsonify({
        'result': 'success',
        'school': points
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)