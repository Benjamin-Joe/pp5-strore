

def items_in_bag(request):
    """Function for calculating cost of items in basker"""
    bag_items = []
    total = 0
    product_number = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_number': product_number,

    }

    return context
