from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from blog.models import Post

def index_blog(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html', context)

def single_blog(request,pid):
    posts = get_object_or_404(Post,id=pid)
    context = {'post':posts}
    return render(request , 'blog/blog-single.html',context)

def test_view(request):
    return render(request,'test.html')