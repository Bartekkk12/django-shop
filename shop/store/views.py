from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout

from .models import Category, Product, Review, Cart, CartItem
from .forms import RegisterForm, LoginForm, AddToCartForm

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

def user_account(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    return render(request, 'store/user_account.html')

def cart(request):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.items.all()
    else:
        cart = None
        cart_items = [] 
           
    context = {'cart_items': cart_items, 'cart': cart}
    
    return render(request, 'store/cart.html', context)

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
    
    if request.method == 'POST':
        form = AddToCartForm(request.POST, product=product)
        
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            flavor = form.cleaned_data['flavor']

            if request.user.is_authenticated:
                cart, _ = Cart.objects.get_or_create(user=request.user)
                cart_item, created = CartItem.objects.get_or_create(cart=cart,product=product,flavor=flavor,defaults={'quantity': quantity})

            if not created:
                cart_item.quantity += quantity
                cart_item.save()
                
            return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = AddToCartForm(product=product)
    
    context = {
        'product': product, 
        'product_reviews': product_reviews, 
        'flavors': flavors, 
        'form': form,
    }
    
    return render(request, 'store/product_detail.html', context)

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    
    return redirect('cart')

def increase_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.quantity += 1
    item.save()
    
    return redirect('cart')

def decrease_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    
    return redirect('cart')