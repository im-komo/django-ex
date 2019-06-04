from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
# def hellopost(request):
#     return HttpResponse('hello from post')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(post)
    return render(request, 'blog/post_detail.html', {'post':post})