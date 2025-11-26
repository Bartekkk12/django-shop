from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('cart/', views.cart, name='cart'),
    
    path('categories/', views.category_list, name='categories'),
    path('categories/<slug:slug>/', views.category_detail, name='category'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
]