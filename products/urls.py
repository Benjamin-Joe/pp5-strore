from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.Products, name='products'),
    path('<product_id>', views.Product_Detail, name='product_detail')
]
