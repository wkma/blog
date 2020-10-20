"""test12_bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,re_path
from app01 import views

from django.views.static import serve
from test12_bbs import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('boot',views.bootstrapcs),
    re_path(r'^register/',views.register,name='reg'),
    re_path(r'^login/',views.login,name='login'),
    #图片验证码相关操作
    re_path(r'^get_code',views.get_code,name="get"),
    #首页
    re_path(r'^$',views.home,name='home'),
    #修改密码
    re_path(r'^set_password/',views.set_password,name="set_pas"),
    #退出登录
    re_path(r'^logout/',views.logout,name='logout'),
    #暴露后端指定文件夹资源
    re_path(r'^media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT}),
    #点赞点踩
    re_path(r'^up_or_down/',views.up_or_down),
    #文章评论
    re_path(r"^comment/",views.comment),
    #后台管理
    re_path(r'^backend/',views.backend),
    #添加文章
    re_path(r'^add/article/',views.add_article),

    #个人站点页面
    re_path(r'^(?P<username>\w+)/$',views.site,name='site'),
    #侧边栏筛选功能
    # re_path(r'^(?P<username>\w+)/category/(\d+)/',views.site),
    # re_path(r'^(?P<username>\w+)/tag/(\d+)/',views.site),
    # re_path(r'^(?P<username>\w+)/archive/(\d+)/', views.site),
    #以上三条url合并成一条
    re_path(r'^(?P<username>\w+)/(?P<condition>category|tag|archive)/(?P<param>.*)/',views.site),

    #文章详情页
    re_path(r'^(?P<username>\w+)/article/(?P<article_id>\d+)/',views.article_detail),





]
