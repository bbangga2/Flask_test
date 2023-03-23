'''
    라우트추가 -> URL을 추가한다는 의미
'''

from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

# 기획서를 기반으로 총 페이지 수 만큼 URL을 준비(뼈대부터 짠다)
# 뼈대를 먼저 잡아서 각 페이지에 해당하는 URL 준비
# blueprint를 사용한다면, 대분류, 중분류(생략가능), 소분류 등 트리구조로  배치
# /login <->(블루프린트) /auth/users/login

@app.route('/')
def home():
    return'helloworld'

# 아래와 같은 url구성은 blueprint를 사용하여 섹션을 나눠서 관리하는 것이 더 낫다
@app.route('/login')
def login():
    return'login page'

@app.route('/signup')
def signup():
    return'signup page'
if __name__=='__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)
