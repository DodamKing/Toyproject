from flask_sqlalchemy import SQLAlchemy # pip install flask_sqlalchemy

db = SQLAlchemy()           #SQLAlchemy를 사용해 데이터베이스 저장

class User(db.Model): 
    __tablename__ = 'user_table'   #테이블 이름 : user_table
    id = db.Column(db.Integer, primary_key = True)   #id를 프라이머리키로 설정
    password = db.Column(db.String(64))     #패스워드를 받아올 문자열길이 
    userid = db.Column(db.String(32))       #이하 위와 동일
    username = db.Column(db.String(8))