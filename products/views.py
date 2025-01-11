from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime

from products.models import Product

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the products index.")

    products = Product.objects.all()
    return render(request, "index.html", { "products": products })

def delete(request, id):
    product = Product.objects.get(id=id)

    if product is None:
        return HttpResponse("Product not found", status=404)
    
    product.delete()
    return redirect("/home")

def details(request):
    return HttpResponse(
        """<h1>Product Details</h1> 
        <hr> 
        <p>Product details page</p>"""
    )
