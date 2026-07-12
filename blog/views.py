from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from blog.models import Post

def index_blog(request):
    return render(request,'blog/blog-home.html')

def single_blog(request):
    return render(request , 'blog/blog-single.html')


def test_view(request , pid):
    post = get_object_or_404(Post,id=pid)
    context = {'post':post}
    return render(request,'test.html' , context)