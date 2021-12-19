from django.shortcuts import render, get_object_or_404
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


def Product_Detail(request, product_id):
    """
    View to render individual product details
    """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)

