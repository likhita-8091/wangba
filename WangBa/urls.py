"""WangBa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path

from app01 import views
from app01.models import User

defaults = dict()
defaults['role'] = 1
defaults['account'] = 'admin'
defaults['password'] = 'admin'
defaults['sex'] = '男'
defaults['u_age'] = 26
defaults['phone'] = 13006293101
defaults['note'] = '超级管理员(默认创建)'

User.objects.update_or_create(defaults=defaults, name="admin")

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^logout/$', views.logout, name='logout'),
    re_path('^$', views.wang_guan_list),

    path('index/', views.wang_guan_list, name='index'),

    path("wang_guan_list/", views.wang_guan_list, name="wang_guan_list"),
    path('wang_guan_add/', views.wang_guan_add, name='wang_guan_add'),
    re_path('^wang_guan_edit/(?P<wang_guan_id>\d+)/$', views.wang_guan_edit, name='wang_guan_edit'),
    re_path('^wang_guan_del/(?P<wang_guan_id>\d+)/$', views.wang_guan_del, name='wang_guan_del'),

    path("hui_yuan_list/", views.hui_yuan_list, name="hui_yuan_list"),
    path('hui_yuan_add/', views.hui_yuan_add, name='hui_yuan_add'),
    re_path('^hui_yuan_edit/(?P<hui_yuan_id>\d+)/$', views.hui_yuan_edit, name='hui_yuan_edit'),
    re_path('^hui_yuan_del/(?P<hui_yuan_id>\d+)/$', views.hui_yuan_del, name='hui_yuan_del'),

    re_path('^(?P<action>wang_guan|hui_yuan)/(?P<_id>\d+)/$', views.get_query),
]
