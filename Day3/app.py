import random
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello.html')

@app.route("/hi")
def hi():
    return render_template('hi.html')

#variable routing : 경로를 변수로 활용한다.
@app.route('/hi/<string:name>')
def higyo(name):
    return render_template('hi2.html', namee=name)


# /cube/<숫자>
# 세제곱 결과를 보여주는 페이지!
@app.route('/cube/<int:num>')
def cube(num):
    return f'{num**3}'

# /lunch/사람이름
# ~~야 ~~먹어
@app.route('/lunch/<string:name>')
def lunch(name):
    menu = ['한식', '중식', '일식', '고기']
    return render_template('menu.html', name=name, food=random.choice(menu))

# / lotto
# 로또 번호 6개를 추천해주는 페이지
@app.route('/lotto')
def lotto():
    lotto = random.sample(range(1,46),6)
    return f'이번주 로또 번호는 {sorted(lotto)}!!'
    
if __name__ == "__main__":
    # python app.py 를 하면 아래의 코드 블록을 실행시킨다.
    app.run(debug=True)