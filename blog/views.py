from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

def index_blog(request):
    return render(request,'blog/blog-home.html')

def single_blog(request):
    return render(request , 'blog/blog-single.html')

