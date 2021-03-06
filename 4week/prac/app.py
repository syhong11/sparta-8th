
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# python decorator(데코레이터)
# 함수를 꾸며주는 함수
# 라우터 기능: 사용자가 접속할 수 있는 URL을 생성
# 사용자가 접속할 수 있는 URL (https://naver.com/)
@app.route('/')
def home():
    # return "Hello World!"
    return render_template('index.html')

@app.route('/mypage')
def mypage():
    return "This is My Page"


# API
# url, header, body
@app.route('/test/get/data', methods=['GET'])
def get_data():
    username_receive = request.args.get('username')
    password_recsive = request.args.get('password')


    data = {
        'test' : 123,
        'tset1' : True,
        'test2' : '스파르타'
    }

    if password_recsive == '1234':
        data['test1'] = False

    return jsonify(data)

@app.route('/test/post/data', methods=['POST'])
def post_data():
    username_receive = request.form['username']
    password_recsive = request.form['password']

    print(username_receive, password_recsive)

    data = {
        'success': True
    }
    return jsonify(data)


# __name__ : 해당 파이썬 파일이 실행되는 위치
# __name__ == '__main__'
# 해당 파이썬 파일이 실행 되었을 때
if __name__ == '__main__':
    # 0.0.0.0 : 허용하는 IP가 모든 IP
    # debug: 디버그 모드(테스트 모드)
    # 에러가 발생했을 때 어디 부분이 에러인지 표시
    # port: 접속 경로 포트
    # localhost:5000
    app.run('0.0.0.0', debug=True, port=5000)