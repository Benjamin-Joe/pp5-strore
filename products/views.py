from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def Products(request):
    """
    View to render products 
    """
    products = Product.objects.all()
    query = None
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You Did Not Search For Anything!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(price__icontains=query)
            products = products.filter(queries) 
    
    context = {
        'products': products,
        'search_term': query
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

