from django.contrib import admin
from django.urls import path , include
from .views import *

app_name = "blog"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , index_blog , name='home-blog'),
    path('<int:pid>' , single_blog , name='single-blog'),
    path('category/<str:cat_name>' , index_blog , name='category'),
    path('author/<str:author_username>' , index_blog , name='author'),
    path('search/' , blog_search , name='search'),
    path('test/' , test_view , name="test"),
]
