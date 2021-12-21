from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal 
from django.conf import settings

def items_in_bag(request):
    """Function for calculating cost of items in basker"""
    bag_items = []
    total = 0
    product_number = 0
    bag = request.session.get('bag', {})
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_number': product_number,

    }

    return context
