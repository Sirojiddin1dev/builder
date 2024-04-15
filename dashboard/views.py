from django.shortcuts import render
from main.models import *

def blog_view(request):
    context={
        'blog': Blog.objects.all().order_by('-id')[:6]
    }
    return render(request,'blog.html' ,context)


def blog_banner_view(request):
    context = {
        'img': Blog.objects.all().order_by('-id')[:2]
    }
    return render(request,'blog.html', context)


def blog_details_view(request):
    return render(request, 'blog-details.html')