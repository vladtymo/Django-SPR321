from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the products index.")


def details(request):
    return HttpResponse(
        """<h1>Product Details</h1> 
        <hr> 
        <p>Product details page</p>"""
    )
