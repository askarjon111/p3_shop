from django.shortcuts import render
from .models import Product


def home_view(request):
    products = Product.objects.all().order_by('-id')[:4]
    return render(request, 'index.html', {'products': products})


def products_view(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'shop.html', {'products': products})


def single_product_view(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})
