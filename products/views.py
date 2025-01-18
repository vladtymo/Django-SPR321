from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from datetime import datetime

from products.forms import ProductForm
from products.models import Product

def index(request):
    products = Product.objects.all()
    return render(request, "index.html", { "products": products })

def create(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, "create.html", { "form": form })
    
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect("/")

    return render(request, "create.html", { "form": form })

def edit(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "GET":
        form = ProductForm(instance=product)
        return render(request, "edit.html", { "form": form })
    
    form = ProductForm(request.POST, request.FILES, instance=product)

    if form.is_valid():

        if product.imageFile:
            product.imageFile.delete()

        form.save()
        return redirect("/")

    return render(request, "edit.html", { "form": form })

def delete(request, id):
    product = get_object_or_404(Product, id=id)
    
    if product.imageFile:
        product.imageFile.delete()

    product.delete()
    return redirect("/")

def details(request, id):
    product = get_object_or_404(Product, id=id)
    
    return render(request, "details.html", { "item": product })
