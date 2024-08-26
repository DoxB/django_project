from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


# class PostList(ListView):   # post_list.html, post-list
#     model = Post
#     # template_name = 'blog/index.html'
#     # ordering = '-pk'
#     # context_object_name = 'posts'

class PostList(ListView):   # post_list.html, post-list
    model = Post
    # template_name = 'blog/index.html'
    ordering = '-pk'
    context_object_name = 'post_list'


# Create your views here.
def about_me(request):
    posts = Post.objects.all() # 1. 쿼리로 데이터를 모두 가져옵니다
    return render(
        request,
        'blog/about_me.html'
    )

def index(request):
    posts = Post.objects.all() # 1. 쿼리로 데이터를 모두 가져옵니다
    # 가져온 데이터는 어디에 뿌려야 하나요? Templates로 보내야겠죠
    return render(
        request,
        'blog/index.html',
        {
            'posts':posts,
            'my_list': ["apple", "banana", "cherry"],
            'my_text': "첫번째 줄 \n 두번째 줄",
            'content' : ["<img src='data/jjangu.png'>", "<img src='data/jjangu.png'>", "<img src='data/jjangu.png'>"],
        }
    )