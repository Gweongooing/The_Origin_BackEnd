### Advanced Mission

---

고객센터 1:1 문의, 답글 모델 만들기

### 미션 내용 : 고객센터 앱에 1:1 문의, 답변 모델 만들기

### 목표

- 예시 화면 기반의 모델링 진행
    - 모델링 : 어떠한 데이터를 저장할 것인지 판단하여 모델 생성, 구성하는 작업
- 데이터베이스, 모델 관계 구성 이해

### 요구사항

- 1:1 문의, 답변 모델 생성
- 1:1 문의 모델 화면, 모델명 : `Inquiry`
- 답변 모델 생성, 모델명 : `Answer`
    - 답변 모델 필드 : 답변 내용, 참조 문의글, 생성자, 생성 일시, 최종 수정자, 최종 수정 일시
- 문의와 답변은 1 - N 관계 구성
    - 문의 1 - 답변 N

### 힌트

- 사용자가 입력하지 않지만 DB에 저장해야하는 데이터가 존재(예 생성자, 생성 일시)
- 모델링 영상 : 2_4_인스타그램게시글로이해하는Models(1)

---

### 만든 결과

- /admin Login 정보
    - ID : admin
    - PW : 0000
- 질문

![image](https://user-images.githubusercontent.com/67627129/163860574-178b0200-2b36-4ef6-9157-62bd89dc7354.png)


- 답변

![image](https://user-images.githubusercontent.com/67627129/163860622-f6c0c114-6edb-43ee-b1d2-1dd6c4760e2b.png)


- 연결 확인
    - inline을 하지 않으면 두개의 Table 연결이 안되서 갱신이 안보임
    - inline을 해서 확인

![image](https://user-images.githubusercontent.com/67627129/163860767-6202a037-5458-4f42-bbe9-41e34a992e8f.png)
![image](https://user-images.githubusercontent.com/67627129/163860797-34fce5ee-3f7a-4742-aef9-c64514d176d9.png)
![image](https://user-images.githubusercontent.com/67627129/163860804-d6decea3-7f14-4def-99d9-561078277f5e.png)


---

### 특이사항

- 요구사항 중 예시 사진
    - 1:1 문의 모델 화면 보다는 모델링만 해도 된다고 확인
    - ![image](https://user-images.githubusercontent.com/67627129/163860090-1ff23282-3091-405c-b23f-53651aea9f1e.png)
    - 모델링을 통해서 화면을 구성하고 하기에는 변수 등이 많아서 모델만 제작
    - 데이터가 잘 만들어 졌는지는 admin을 통해서 확인을 햇기 때문에 연결만 하면 동일하게 동작 가능
    - 현재 시점(3주차 강의 완료)에서 포함된 내용이 아닌 이번주(4주차)강의를 통해서 추가적으로 화면을 구성하는 것이 더 도움이 된다고 생각
    - 모델과 화면을 연결해주는 부분을 

- 1:N 관계가 중요하다고 생각
    - 필드에 외래키(Forignkey)를 사용해서 연결하고 삭제시 같이 삭제되는 것을 확인하는 것이 이번 모델링의 목적이라고 생각
    - 화면연결보다는 Admin에서 테스트를 통해서 확인
