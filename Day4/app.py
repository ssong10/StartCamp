# 0 . flask 패키지 가져오기
import random
from flask import Flask, render_template, request

# 1. app 설정
app = Flask(__name__)

# 2. 요청 경료(route) + 함수 만들기
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<string:name>')
def hello(name):
    return render_template('hello.html',name = name)

@app.route('/lunch')
def lunch():
    menus = ['레드코코넛누들','소불고기' , '삼계탕', '싸이버거', '치킨']
    pick = random.choice(menus)
    return render_template('lunch.html',menus= menus,pick=pick)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    # 사용자가 보낸 데이터를 받아와서
    text = request.args.get('say')
    textext = request.args.get('saysay')

    print(request.args)
    # 템플릿에 넘겨준다.
    return render_template('pong.html', text=text,textext=textext)

@app.route('/question')
def question():
    return render_template('question.html')

@app.route('/answer')
def answer():
    character = ['고독한','배고픈' , '성공한', '엉뚱한', '수십억을 가지고 있는','이상한','천재','부유한','퇴근 일찍 하는']
    pick = random.choice(character)
    name = request.args.get('name')
    job = request.args.get('job')
    return render_template('answer.html', pick=pick, job=job, name=name)

@app.route('/lotto')
def lotto():
    return render_template('lotto.html')

@app.route('/lotto_result')
def lotto_result():
    name = request.args.get('name')
    num = request.args.get('num')
    random.seed(num)
    numbers = random.sample(range(1,46),6)
    return render_template('lotto_result.html', num=num , name=name, numbers = numbers)
if __name__ == '__main__':
    app.run(debug=True)
