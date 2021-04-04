"""mysiteday62 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    # url(r'^home/', views.publisher_list),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),

    # 出版社相关
    url(r'^publisher_list/', views.publisher_list),
    url(r'^add_publisher/', views.AddPublisher.as_view()),
    # url(r'^add_publisher/', views.add_publisher),

    url(r'^delete_publisher/', views.delete_publisher),
    url(r'^edit_publisher/', views.edit_publisher),

    # 书相关的对应关系
    url(r'^book_list/', views.book_list,name='book_list'),
    url(r'^add_book/', views.add_book),  # 添加书籍
    url(r'^delete_book/', views.delete_book),  # 删除书籍
    # url(r'^edit_book/', views.edit_book),  # 编辑书籍
    url(r'^edit_book/$', views.edit_book,name='edit_book'),  # 编辑书籍
    
    # 作者相关的对应关系
    url(r'^author_list/', views.author_list),  # 展示作者
    url(r'^add_author/', views.add_author),  # 添加作者
    url(r'^delete_author/', views.delete_author),  # 删除作者
    url(r'^edit_author/', views.edit_author),  # 编辑作者

    # url(r'^test/', views.test),
    url(r'^test/', views.test,name='test'),
    url(r'^upload/$', views.upload),

    # 商品展示
    url(r'^goods_list/', views.store,name='store'),
    url(r'^goods_show/', views.show,name='store'),

    #Sweetalet插件
    url(r'^sweetalert_demo/', views.show),
]
