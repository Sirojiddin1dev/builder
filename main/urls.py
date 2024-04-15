from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index_url'),
    path('product',product_view, name='product_url')
]