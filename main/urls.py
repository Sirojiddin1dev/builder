from django.urls import path
from .views import *

urlpatterns = [
    path('product-fasad/',product_fasad_view, name='fasad_product_url'),
    path('product-sokol/',product_sokol_view, name='sokol_product_url'),
    path('product-forma/',product_forma_view, name='forma_product_url'),
    path('', product_view, name='product_url'),
    path('checkout/<int:pk>/', checkout_view, name='checkout_url'),
    path('blog/', blog_view, name='blog'),
    path('foto/', portfolio_view, name='portfolio_url'),
    path('blog-details/<int:pk>/', blog_details_view, name='blog-details'),
    path('product-dateil/<int:pk>/', product_details, name='product_details_url')
]