from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout

from .models import Category, Product, Review, User
from .forms import RegisterForm, LoginForm

# Create your views here.

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    reviews = Review.objects.all()
    context = {'categories': categories, 'products': products, 'reviews': reviews}
    
    return render(request, 'store/home.html', context)

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'store/register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'store/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

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