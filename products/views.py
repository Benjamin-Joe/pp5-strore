from django.shortcuts import render
from .models import Product


def Products(request):
    """
    View to render products 
    """
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)

