from django.shortcuts import render
from main.models import *

def blog_view(request):
    context={
        'blog': Blog.objects.all().order_by('-id')[:6]
    }
    return render(request,'blog.html')


def blog_banner_view(request):
    context = {
        'img': Blog.objects.last()
    }
