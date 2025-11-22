from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.category_list, name='categories'),
    path('categories/<slug:slug>/', views.category_detail, name='category'),
]