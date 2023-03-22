# 홈페이지 작성, 디버깅 모드, 포트 5000번, 홈페이지는 화면에 "helloworld"만 출력

from flask import Flask, render_template, jsonify, request, redirect, url_for
# 화면 랜더링할 때 render_template, json 응답 받을때 jsonify, 

# 2. 앱 만들기
app = Flask(__name__)

# 3. 라우팅
##@는 함수안에 함수, 데코레이터
@app.route('/')
def home():
    return'helloworld'

# 4. 서버가동
if __name__=='__main__':
    # 웹 상에 기본 포트: http => 80 => 생략 가능
    # 80으로 들어온걸 내부적으로 5000으로 변환한다? -> Flask 단독으로는 서비스 안함, 웹서버를 붙여야함 
    ## 나중에 웹서버(apache 서버(php, java), nginx)와 연동
    app.run(debug=True, host='0.0.0.0', port=5000)
    # 포트번호 안쓰면 5000, 어디서든지 접근 가능하는 호스트는 0.0.0.0