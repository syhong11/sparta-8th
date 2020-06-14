from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('localhost', port=27017)
db = client.schoolzonedb

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('maptest.html')

@app.route('/api/list')
def star_retreive():
    stars = list(
        db.school.find({}, {'_id': False, 'Latitude': 1, 'Longitude': 1)
    return jsonify({
        'result': 'success',
        'school': school
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)