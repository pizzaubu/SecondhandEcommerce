from django.shortcuts import render

def home(request):
    return render(request,"shop/index.html")

def register(request):
    return render(request,"shop/register.html")

def main(request):
    return render(request,"shop/main.html")

def products(request):
    return render(request,"shop/products.html")
