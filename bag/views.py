from django.shortcuts import render, redirect

"""
Code below came mostly from Code Institute
"""


def bag(request):
    """
    View for the basket page, this contains
    all of the users items and purchases
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Adding items to shopping basket"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)