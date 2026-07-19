from django import template
from blog.models import *

register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts 


@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts 

@register.filter
def snippet(value,arg=20):
    return value[:arg] + "..."


@register.inclusion_tag('blog/popular-posts.html')
def lastest_posts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {"posts":posts}


@register.inclusion_tag('blog/blog-categories.html')
def postCategory():
    categories = Category.objects.all()
    cat_dict = {}

    for name in categories:
        cat_dict[name] = Post.objects.filter(
            status=1,
            category=name
        ).count()

    return {
        "categories": cat_dict
    }