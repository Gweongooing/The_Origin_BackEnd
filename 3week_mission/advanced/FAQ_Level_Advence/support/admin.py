from django.contrib import admin

from .models import inquiry, answer

class answerInline(admin.TabularInline):
    model = answer
    extra = 1
    min_num = 0
    max_num = 5
    verbose_name = '댓글'
    verbose_name_plural = '댓글'

@admin.register(inquiry)
class inquiryModelAdmin(admin.ModelAdmin):
# inquiry 보기위한 table 컬럼 구성
    list_display = ('id', 'category_list', 'title', 'mail_add', 'text_msg', 'content', 'writer', 'created_at', 'modified_at')
    inlines = [answerInline]

@admin.register(answer)
class answerModelAdmin(admin.ModelAdmin):
# answer 보기위한 table 컬럼 구성
    list_display = ('id', 'content', 'inquiry', 'writer', 'create_at')
