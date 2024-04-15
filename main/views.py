from django.shortcuts import render
from .models import *


def index_view(request):
    context = {
        'product': Product.objects.all().order_by('-view')[:5],
        'blog': Blog.objects.all().order_by('-id')[:5],
    }
    return render(request, 'index.html', context)


def product_view(request):
    categories = Category.objects.filter(is_active=True).order_by('-id')[:3]
    category = request.GET.get('category')
    context = {
        'categories': categories,
        'selected_category': category,
        'product': Product.objects.all()
    }
    return render(request, 'shop.html', context)
