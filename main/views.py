from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.http import HttpResponseServerError


def portfolio_view(request):
    context = {
        'photo': Gallery.objects.all().order_by('-id')[:32]
    }
    return render(request, 'portfolio.html', context=context)


def product_fasad_view(request):
    try:
        products = Product.objects.filter(category="Fasad")
        paginator = Paginator(products, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        count = products.all().count()
        context = {
            'product': page_obj,
            'page_obj': page_obj,
            'count': count
        }
        return render(request, 'shop-four-columns.html', context)
    except Exception as e:
        print(e)


def product_sokol_view(request):
    try:
        products = Product.objects.filter(category="Sokol")
        paginator = Paginator(products, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        count = products.all().count()
        context = {
            'product': page_obj,
            'page_obj': page_obj,
            'count': count
        }
        return render(request, 'shop-four-columns.html', context)
    except Exception as e:
        print(e)


def product_forma_view(request):
    try:
        products = Product.objects.filter(category="Forma")
        paginator = Paginator(products, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        count = products.all().count()
        context = {
            'product': page_obj,
            'page_obj': page_obj,
            'count': count
        }
        return render(request, 'shop-four-columns.html', context)
    except Exception as e:
        print(e)


def product_view(request):
    products = Product.objects.all()
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count = products.all().count()
    context = {
        'product': page_obj,
        'page_obj': page_obj,
        'count': count
    }
    return render(request, 'shop-four-columns.html', context)


def blog_view(request):
    try:
        blog = Blog.objects.all()
        paginator = Paginator(blog, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'blog': page_obj,
            'page_obj': page_obj
        }
        return render(request,'blog.html', context)
    except Exception as e:
        print(e)


def blog_details_view(request, pk):
    blog = Blog.objects.get(pk=pk)
    context={
        'blog_details': blog
    }
    return render(request, 'blog-details.html', context)


def product_details(request,pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product,
        'products': Product.objects.all().order_by('-id')[:4]
    }
    return render(request, 'product-details.html',context)


def checkout_view(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    if request.method == "POST":
        name = request.POST['name']
        quantity = request.POST['quantity']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        country = request.POST['country']
        Checkout.objects.create(
            name=name,
            product=product,
            quantity=quantity,
            email=email,
            phone_number=phone_number,
            address=address,
            country=country,
        )
        return redirect('checkout_url', product.pk)
    return render(request, 'checkout.html', context)
