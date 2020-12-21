---
title : "[프로그래머스인공지능스쿨]Flask로 CRUD 구현하기"
data : 2020-12-21 00:15:28 -0400
categories : 프로그래머스인공지능스쿨
---
Flask로 CRUD(Create, Read, Update, Delete) 4가지 logic을 구현해보자!  

- [x] Create 구현  
    - `POST`에 해당한다  
- [x] Read 구현  
    - `GET`에 해당한다  
- [x] Update 구현  
    - `PUT`에 해당한다
- [x] Delete 구현  
    - `DELETE`에 해당한다
- [x] POST 요청이 들어올 때마다 id가 하나씩 증가하여 menu 리스트에 추가될 수 있도록 코드를 수정   
    - 새로운 menu를 추가하는 POST 영역에서 id가 4로 고정되어있는 문제가 발생합니다.
    - POST 요청이 들어올 때마다 id가 하나씩 증가하여 menu 리스트에 추가될 수 있도록 코드를 수정해주세요.
    - global 변수 사용함!  
- [ ] 데이터베이스 연동하기  
    - 이 API는 서버를 재시작하면 모든 정보가 리셋되는 치명적인 문제가 있었습니다. 이를 해결하기 위해 데이터만을 저장하는 데이터베이스를 도입하여 Flask과 연동할 필요가 생겼습니다.  
    - SQL과 ORM 중 하나를 선택하여 데이터베이스와 Flask app을 연동해봅시다. (즉, 자원에 CRUD가 발생하면 이 정보가 데이터베이스에 저장되어야합니다.)  

```python
from flask import Flask, jsonify, request
# jsonify : 파이썬의 딕셔너리 타입(menus)을 json이라는 데이터 저장 방식으로 바꿔줌
# request : HTTP request를 다룰 수 있는 모듈
app = Flask(__name__) # Flask를 바탕으로 한 객체 생성. 인자로 __name__전달. Flask에 이름을 앱으로 넣어준다는 의미

menus = [
    {"id":1, "name":"Espresso", "price":3800},
    {"id":2, "name":"Americano", "price":4100},
    {"id":3, "name":"CafeLatte", "price":4600},
]


# 홈 디렉토리
@app.route('/') # 이 주소를 요청받았을때 밑에 있는 함수를 실행하라.
def hello_code():
    return 'Hello World!'


# GET /menus : 자료를 가지고 온다
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})
# menus는 리스트로 json으로 변환할 수 없다. 
#따라서 menus를 value로 하는 새로운 딕셔너리를 만들어준다.

new_id = 4
# POST /menus : 자료를 자원에 추가한다.
# @app.route는 기본적으로 methods=['GET']라고 되어있다.
# 나머지 HTTP 동작들, POST 등은 직접 명시를 해야한다.
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    global new_id
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() # {"name" : ..., "price": ...}
    # request는 자동적으로 클라이언트가 서버에 POST로 요청할때 담긴 자료가 있다.
    # 따라서 이를 get_json()으로 파싱해주면 딕셔너리 형태로 담기게 된다.
    new_menu = {
        "id" : new_id,
        "name" : request_data['name'],
        "price" : request_data['price'],
    }
    new_id += 1
    menus.append(new_menu)
    return jsonify(new_menu)


# PUT /menu/<int:id> : 해당하는 id에 해당하는 데이터를 갱신합니다. (HTTPRequest의 Body에 갱신할 내용이 json으로 전달됩니다.)
@app.route('/menus/<int:id>', methods=['PUT'])
def put_menu(id):
    update_data = request.get_json()
    try:
        menus[id-1]['name'] = update_data['name']
        menus[id-1]['price'] = update_data['price']
        return jsonify(menus[id-1])
    except Exception as e:
        print(e)
        return 'There was a problem!'


# DELETE /menu/<int:id> : 해당하는 id에 해당하는 데이터를 삭제합니다.
@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    try:
        del menus[id-1]
        return jsonify(menus)
    except Exception as e:
        print(e)
        return 'There was a problem!'


if __name__ == '__main__':
    app.run()
```