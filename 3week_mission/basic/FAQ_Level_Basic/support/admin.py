from django.contrib import admin

from .models import faq

@admin.register(faq)
class faqModelAdmin(admin.ModelAdmin):
# faq 보기위한 table 컬럼 구성
    list_display = ('id', 'category_list', 'title', 'inquiry_content', 'answer_content', 'created_at', 'modified_at', 'writer')
