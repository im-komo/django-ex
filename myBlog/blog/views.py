from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def hellopost(request):
#     return HttpResponse('hello from post')

def post_list(request):
    return render(request, 'blog/post_list.html', {})