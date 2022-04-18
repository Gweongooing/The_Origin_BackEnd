from django.db import models

# to=user 사용자와 연결하기 위한 import
from django.contrib.auth import get_user_model
User = get_user_model()

# 카테고리, 제목, 이메일, 문자메시지, 내용, 이미지
class inquiry(models.Model):
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
    title = models.CharField(max_length=30)     # 제목 글자수 제한
    mail_add = models.EmailField('이메일')      # 이메일
    text_msg = models.CharField(max_length=40, verbose_name='문자메시지')      # 문자메시지
    content = models.TextField('질문')      # 질문 내용
    image = models.ImageField(verbose_name='이미지')
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField('생성일시', auto_now_add=True)      # 작성시(지금) 시간 
    modified_at = models.DateTimeField('최종 수정일시', auto_now=True)      # 수정(객체등록) 자동 업데이트


# 답변 내용, 참조 문의글, 생성자, 생성 일시, 최종 수정자, 최종 수정 일시
class answer(models.Model):
    content = models.TextField(verbose_name='답변')     # 답변 내용
    inquiry = models.ForeignKey(to='inquiry', on_delete=models.CASCADE)        #inquiry 삭제시 answer 전체 삭제 # 참조 문의글??
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    create_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)        # 답변 작성일 (갱신)
    # inline으로 되면서 답변도 질문객체로 인식 되어 최종수정일시 수정됨
