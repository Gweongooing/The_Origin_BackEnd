### Basic Mission

---

<aside>
💡 사용자와 소통창구, 고객센터 앱과 FAQ 모델 만들기

</aside>

### 미션 내용 : 고객센터 앱과 FAQ 모델 만들기

- 사용자에게 자주묻는질문 제공을 위한 고객센터앱, 자주묻는질문 모델 생성

### 목표

- 장고 ORM Models, Fields에 대한 이해

### 요구사항

- 고객센터 앱 생성
    - 앱명 : `support`
- FAQ 모델 생성
    - 모델명 : `Faq`
    - 필드 : 질문, 카테고리, 답변, 생성자, 생성일시, 최종 수정자, 최종 수정일시

### 힌트

- `django-admin startapp support`
- 카테고리 사용 시 `choices` 사용
- 카테고리 목록 : 일반, 계정, 기타
- [https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types](https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types)
- [https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options](https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options)

---

### 만든 결과

- /admin 확인
    - 계정 : admin
    - P/W : 0000

- 글 Upload
    - category list 확인

![image](https://user-images.githubusercontent.com/67627129/163858344-11d1876a-5879-4c93-8c8c-505a6d2a9c68.png)

- 데이터 변경에 따른 최종 수정일자 확인

![image](https://user-images.githubusercontent.com/67627129/163858865-0ea78f9c-c4b5-4db2-88e6-6d549eb21238.png)

---

### 특이사항

- 요구사항 확인
    - 모델(=테이블)만 제작
    - 질문, 답변 모두 한 모델 안에 있음

- 부족한 부분
    - 자동 로그인이 아니다
    - 생성자, 최종 수정자 두 가지는 로그인 정보가 없어서 계정 정보로 선택

