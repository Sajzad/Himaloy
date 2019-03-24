from django.urls import path
from . import views

urlpatterns=[

path('index/', views.index_view,name='index'),
path('blog/', views.blog_view,name='blog'),
# path('post/<id>/', views.post,name='post'),
path('search/', views.search,name='search'),
path('post-detail/<post_id>/', views.post_detail, name='post-detail'),
path('python-post-list/', views.python_list,name='python-post-list'),
path('c-post-list/', views.C_list, name='c-post-list'),



]
