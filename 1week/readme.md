Project Lion The Origin BackEnd course
=============
   
1Week 강의 내용
-------------
   
   
1Week basic Mission
-------------
> Lotto Number expert
* 입력
  - 없음
* 출력
  - 로또번호 6자리 출력

> 특이사항
> * site 경로 차이
>     test

1Week challenge Mission
-------------
> Lotto Number expert
* 입력
* 출력

# 1차 미션

### Basic Mission

---

<aside>
💡 로또 번호 추출기 만들기

</aside>

### 미션 내용 : 로또 번호 추출기 구현

- 사용자가 웹사이트에 접속하여 ‘로또 번호 추출하기’ 버튼을 클릭 시 [1, 5, 30, 21, 20, 40, 45] 형태의 로또번호가 출력

### 목표

- 장고의 디자인패턴 및 흐름에 대한 이해 `urls.py` → `views.py` → `template`→ `views.py`
- 파이썬 구현 능력 향상

### 입력

- 없음

### 출력

- 로또번호 7자리
- 출력 화면

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ac977b1f-085d-468b-abd0-b4f27e255f3e/Untitled.png)

### 가이드

- 기존 `first-django` 프로젝트의 `demo` 앱의 `views.py`에 로또 번호 추출 요청을 처리할 수 있는 함수를 작성
- [`urls.py`](http://urls.py) 새 URL 패턴 추가
- [`views.py`](http://views.py) 로또번호 요청 URL 처리 함수 작성

### 힌트

- 번호 추출 시 `random` 패키지 활용
    - 공식문서 : [https://docs.python.org/ko/3/library/random.html](https://docs.python.org/ko/3/library/random.html)
    - `random.randint(1,45)`
    - `random.sample(list,7)`

### Challenge Mission

---

<aside>
💡 로또 번호 추출기 만들기 2 : 추출 게임 선택, 입출력 분리

</aside>

### 미션 내용 : 로또 번호 추출기2 - 입력, 출력 분리

- (추가내용) 사용자가 뽑고자 하는 게임 수 선택
- (추가내용) 로또 번호 추출 페이지와 로또 번호 생성 결과 페이지 분리
    - 결과 페이지에서 입력 페이지로 이동할 수 있도록 a 태그 사용
- 그 외 Basic 미션과 동일

### 목표

- 웹 프로그래밍의 기초 입력, 결과 페이지 및 기능 분리 학습
- 클라이언트, 서버 요청 응답에 대한 학습
- from, input 태그를 사용한 서버로 데이터 전달 학습

### 입력

- 뽑고자 하는 게임 수(숫자)

### 출력

- 입력 페이지
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e52f4176-0e20-4408-8652-1da2666ba426/Untitled.png)
    
- 결과 페이지
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/09f4b8ce-42d5-4370-b12a-c38d95c88d5d/Untitled.png)
    

### 가이드

- 시나리오 : 입력 페이지 → 결과 페이지
- 입력 페이지는 ‘로또 번호 추출하기’ 버튼의 HTML 응답
- 출력 페이지는 추출된 로또 번호를 출력한 HTML 응답
- 입력 URL : `/lotto/` , 결과 URL : `/lotto/result/`

### 힌트

- 입력용, 결과용 `urls.py`, `views.py`, `html`  2개 씩 필요
- `<form action="/lotto/result/"> ...`
