from flask import Flask, render_template, url_for, request, redirect
import os
from models import db
from models import User

app = Flask(__name__)

@app.route('/')
def Index():
    return ('<h1>Hello Flask!!</h1> <h2><a href="index">이곳을 누르고 사이트로 이동</a></h2>')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/elements')
def elements():
    return render_template('elements.html')

@app.route('/generic')
def generic():
    return render_template('generic.html')

@app.route('/board')
def board():
    return render_template('board.html')

@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')
    else:
         #회원정보 생성
        userid = request.form.get('userid') 
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re_password')
        print(password) # 들어오나 확인해볼 수 있다. 

        if not (userid and username and password and re_password) :
            return '<a href="sign_up"> 모두 입력해주세요 </a>'
        elif password != re_password:
            return '<a href="sign_up"> 비밀번호를 확인해주세요 </a>'
        else: #모두 입력이 정상적으로 되었다면 밑에명령실행(DB에 입력됨)
            user = User()         
            user.password = password           #models의 FCuser 클래스를 이용해 db에 입력한다.
            user.userid = userid
            user.username = username      
            db.session.add(user)
            db.session.commit()
        return ('회원가입 완료 <p><a href="index">Home으로 돌아가기</a></p>')
    

if __name__=='__main__':
    basedir = os.path.abspath(os.path.dirname(__file__))  # database 경로를 절대경로로 설정함
    dbfile = os.path.join(basedir, 'db.sqlite') # 데이터베이스 이름과 경로
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True     # 사용자에게 원하는 정보를 전달완료했을때가 TEARDOWN, 그 순간마다 COMMIT을 하도록 한다.라는 설정
    #여러가지 쌓아져있던 동작들을 Commit을 해주어야 데이터베이스에 반영됨. 이러한 단위들은 트렌젝션이라고함.
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   # True하면 warrnig메시지 유발, 

    db.init_app(app) #초기화 후 db.app에 app으로 명시적으로 넣어줌
    db.app = app
    db.create_all()   # 이 명령이 있어야 생성됨. DB가

    app.run(host='127.0.0.1', port=5000, debug=True)

# pip freeze > requirements.txt
# pip install -r requirements.txt