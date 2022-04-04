"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# View와 연결
import lotto_advence.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # lotto -> Main Page.html로 실행
    path('lotto/', lotto_advence.views.Main_Page, name='Main_Page'),
    # Main_Page.html에서 result로 요청시 result Page
    path('lotto/result/', lotto_advence.views.Result_page, name='Result_page')
]
