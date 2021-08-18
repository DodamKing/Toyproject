from flask import Flask, render_template, url_for

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

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

if __name__=='__main__':
    app.run()

app.run(host='127.0.0.1', port=5000)