from django.shortcuts import render
from .models import Product

# Create your views here.

def shop(request):
    """A view that displays the shop page"""
    products = Product.objects.all()
    return render(request, "shop.html", {"products": products})