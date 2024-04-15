from django.shortcuts import render
from .models import *


def index_view(request):
    context = {
        'product': Product.objects.all().order_by('-view')[:5],
        'blog': Blog.objects.all().order_by('-id')[:5],
    }
    return render(request, 'index.html', context)

