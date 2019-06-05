from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .PostForm import PostForm


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

def post_new(request, pk=None):
    if pk==None:
        form = PostForm()
        return render(request, 'blog/post_new.html', {'form': form})
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_new.html', {'form': form})