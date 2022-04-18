from django.db import models

# to=user 사용자와 연결하기 위한 import
from django.contrib.auth import get_user_model
User = get_user_model()

class faq(models.Model):
    # Choices로 연결하기 위한 카테고리 목록
    category_Choices = [
        ('ge', '일반'), #General
        ('ad', '계정'), #admin
        ('et', '기타'), #etc
    ]  

    category_list = models.CharField(
        max_length=2,
        choices=category_Choices,
    )
    title = models.CharField(max_length=20) # 제목 20글자로 제한
    inquiry_content = models.TextField('질문')      # 질문 내용
    answer_content = models.TextField(verbose_name='답변')     # 답변 내용
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)    # 답변과 질문이 같은 테이블 & 분리방법 모르겠음
    created_at = models.DateTimeField('생성일시', auto_now_add=True)      # 작성시(지금) 시간 
    modified_at = models.DateTimeField('최종 수정일시', auto_now=True)      # 수정(객체등록) 자동 업데이트
