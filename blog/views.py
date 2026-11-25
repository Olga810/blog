from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

# Редирект с главной страницы на список постов
def home_redirect(request):
    return redirect('blog:post_list')

# Список всех постов
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

# Просмотр одного поста
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def old_post_redirect(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return redirect(post, permanent=True) 
