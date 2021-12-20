from django.shortcuts import render


def bag(request):
    """
    View for the basket page, this contains
    all of the users items and purchases
    """
    return render(request, 'bag/bag.html')
