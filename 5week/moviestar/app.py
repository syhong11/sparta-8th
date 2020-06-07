from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('localhost', port=27017)
db = client.dbsparta


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/list')
def star_retreive():
    stars = list(
        db.mystar.find({}, {'_id': False}).sort('like', -1)
    )
    return jsonify({
        'result': 'success',
        'stars': stars
    })


@app.route('/api/like', methods=['POST'])
def star_like():
    name_receive = request.form['name_give']
    star = list(db.mystar.find({'name': name_receive}))
    if len(star) == 0:
        return jsonify ({
            'result': 'fail'
        })
    db.mystar.update_one(
        {'name': name_receive}, 
        {'$set': {
            'like': star[0].get('like', 0) +1
        }}
    )

    return jsonify({
        'result': 'success'
    })

@app.route('/api/delete', methods=['POST'])
def star_delete():
    name_receive = request.form['name_give']
    db.mystar.delete_one({'name': name_receive})
    return jsonify({
        'result': 'success'
    })



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)