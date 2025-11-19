from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404


# Create your views here.

def index(request):
    return render(request,"products/index.html")

def products(request):
    return render(request,"products/products.html")

def products_list(request):
    items = Product.objects.all()  # Get all products from DB
    return render(request, 'products/products.html', {'products': items})

def product_detail(request, pk):
    item = get_object_or_404(Product, pk=pk)
    return render(request, 'products/detail.html', {'product': item})
