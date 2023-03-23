'''
    - POST방식으로 데이터 전송하기
        - 클라이언트 ( Json, Xml, Text, Form(키=값&키=값...), Form-encode, Graphql, Binary ) 
        - form 전송: 화면 껌벅(전환이 됨), (Form, Form-encode 형식)
                <form action="http://127.0.0.1:5000/link" method="post"> 
                    <input name="name" value="hello"/>
                    <input name="age" value="100"/>
                    <input type="submit" value="전송"/>
                </form>
        - ajax(jQuery로 표현) # 무게중심이 클라이언트에 있다. 화면은 껌벅이지 않음 
            - ( Json, Xml, Text, Form(키=값&키=값...), Form-encode, Graphql, Binary ) 방식 가능
            $.post({
                url:"http://127.0.0.1:5000/link",
                data:name=hello&age=100,
                success:( res ) => {},
                error:( err ) => {}
            })
    - 서버
        - post 방식 데이터 추출
        - name = request.form.get('name')
        - age = request.form.get('age') 

    - /link족으로 요청하는 방식은 다양할 수 있다. 단, 사이트 설계상 한가지로만 정의되어있다면,
      다른방식의 접근은 모두 비정상적인 접근이다(웹 크롤링, 스크래핑, 해킹등이 대상)
      이런 접근을 필터링 할 것인가? 보안의 기본적인 사항
'''

from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

# @app.route() -> 아무것도 안쓰면 기본적으로 get방식
# 메소드 추가는 -> methods=['POST',...]
@app.route('/login', methods=['POST','GET'])
def login():
    # method 별 분기
    if request.method == 'GET':
        return "helloworld"
    else: #post
        # request.form['uid'] #값이 누락되면 서버 셧다운이 된다. 사용 금지
        # 1. 로그인 정보 획득 
        uid = request.form.get('uid')
        upw = request.form.get('upw')  # 암호는 차후에 암호화 해야 한다(관리자도 볼 수 없다)
        # 2. 회원 여부 쿼리
        return redirect('https://www.naver.com') # 요청을 다른 url로 포워딩
        # 3. 회원이면
            # 3-1. 세션 생성, 기타 필요한 조치 수행
            # 3-2. 서비스 메인 화면으로 이동
        # 4. 회원 아니면
            # 4-1. 적당한 메시지 후 다시 로그인 유도

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)