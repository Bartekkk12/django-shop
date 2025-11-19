from django.shortcuts import render, redirect

from .models import Category, Product, Review

# Create your views here.

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    reviews = Review.objects.all()
    context = {'categories': categories, 'products': products, 'reviews': reviews}
    
    return render(request, 'store/home.html', context)