'''
- 클라이언트 코드, 클라이언트는 골라서 쓴다. 
    - GET방식으로 데이터 전송하기
        - 링크 (키=값&키=값...) 이걸 누르면 get방식으로 데이터 전송하는 것, 그자체가 화면 전환
            - 상세값을 표현할 때,게시판의 글 상세 내용 볼떄
            <a href="http://127.0.0.1:5000/link?name=hello&age=100">링크</a>
        - form 전송: 사용자에게 입력을 받을 때 쓴다, 가입 등록 검색에 사용, 화면 껌벅(전환이 됨)
            <form action="http://127.0.0.1:5000/link" method="get"> # 태그는 속성을 가질 수 있다. 
                <input name="name" value="hello"/>
                <input name="age" value="100"/>
                <input type="submit" value="전송"/>
            </form>
        - ajax(jQuery로 표현) # 무게중심이 클라이언트에 있다. 화면은 껌벅이지 않음 
            - 검색할 때 
            $.get({
                url:"http://127.0.0.1:5000/link",
                data:name=hello&age=100,
                success:( res ) => {},
                error:( err ) => {}
            })
    - 서버
        - get 방식 데이터 추출
        - name = request.args.get('name')
        - age = request.args.get('age') #변수는 데이터베이스에서 유래된 컬럼을 주로 사용 

    - /link족으로 요청하는 방식은 다양할 수 있다. 단, 사이트 설계상 한가지로만 정의되어있다면,
      다른방식의 접근은 모두 비정상적인 접근이다(웹 크롤링, 스크래핑, 해킹등이 대상)
      이런 접근을 필터링 할 것인가? 보안의 기본적인 사항
'''

from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route('/link')
def link():
    # age = request.args['age'] -> 데이터 누락시 서버 셧다운됨, 절대 사용하면 안됨. 
    # age = request.args.get('age') -> 데이터 누락시 None이 나와서 예외처리 가능함 
    name = request.args.get('name')
    age = request.args.get('age')
    return'[%s] [%s]' %(name, age)

@app.route('/test')
def test():
    # 엔트리포인트(진입로, 프로그램 시작점)과 같은 경로에 temlpates/test.html 생성
    return render_template('test.html')

if __name__=='__main__':
    app.run(debug=True)
