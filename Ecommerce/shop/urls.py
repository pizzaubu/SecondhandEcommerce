from django.urls import path
from . import views

urlpatterns = [
    path('main',views.main,name='main'),
    path('home',views.home,name='home'),
    path('products',views.products,name='products'),
    path('register',views.register,name='register'),
]