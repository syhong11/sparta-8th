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
    # 1. 클라언트에서 좋아요 누른 배우 정보를 받아오기
    # 2. 해당 배우의 like 값을 +1 시킴
    name_receive = request.form['name_give']
    star = list(db.mystar.find({'name': name_receive}))
    if len(star) == 0:
        # 조회하는 영봐 배우가 정보가 없을 때
        return jsonify({
            'result': 'fail'
        })
    # star[0].get('like', 0) > star 리스트의 첫번째 원소의 키가 like의 value 조회하는데 like 키가 없으면
    # 기본 값으로 0으로 채워준다.
    db.mystar.update_one(
        {'name': name_receive},
        {'$set': {
            'like': star[0].get('like', 0) + 1
        }}
    )

    return jsonify({
        'result': 'success'
    })


@app.route('/api/delete', methods=['POST'])
def star_delete():
    # 1. 클라이언트에서 영화 배우 이름을 받아오기
    # 2. 해당 배우의 데이터를 삭제
    name_receive = request.form['name_give']
    db.mystar.delete_one({'name': name_receive})
    return jsonify({
        'result': 'success'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)