from django.contrib import admin
from django.urls import path , include
from .views import *

app_name = "blog"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , index_blog , name='home-blog'),
    path('single/' , single_blog , name='single-blog'),
]
