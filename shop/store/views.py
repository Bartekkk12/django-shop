from django.shortcuts import render, get_object_or_404

from .models import Category, Product, Review, Flavor

# Create your views here.

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    reviews = Review.objects.all()
    context = {'categories': categories, 'products': products, 'reviews': reviews}
    
    return render(request, 'store/home.html', context)

def category_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    
    return render(request, 'store/category_list.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    context = {'category': category, 'products': products}
    
    return render(request, 'store/category_detail.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product_reviews = Review.objects.filter(product=product)
    flavors = product.flavors.all()
    context = {'product': product, 'product_reviews': product_reviews, 'flavors': flavors}
    
    return render(request, 'store/product_detail.html', context)