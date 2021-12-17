from django.shortcuts import render

def index(request):
    """
    View for homepage
    """
    return render(request, 'home/index.html')
