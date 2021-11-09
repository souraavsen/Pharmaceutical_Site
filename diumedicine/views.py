from django.shortcuts import render
from .models import Products


# Create your views here.

def index(request):
    prods = Products.objects.all()
    return render(request, "index.html", {"prods": prods})


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def products(request):
    prods = Products.objects.all()
    return render(request, "shop.html", {'prods': prods})


def product_details(request, product_name):
    selected_pro = Products.objects.get(slug=product_name)
    return render(request,"shop-single.html", {'selected_pro': selected_pro})
