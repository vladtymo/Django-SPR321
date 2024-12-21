from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

tasks = [
    {
        "title": "Buy groceries",
        "description": "Milk, Bread, Cheese, Eggs",
        "completed": True,
        "deadline": datetime(2023, 10, 10),
    },
    {
        "title": "Read a book",
        "description": "Finish reading 'To Kill a Mockingbird'",
        "completed": False,
        "deadline": datetime(2023, 10, 15),
    },
    {
        "title": "Workout",
        "description": "30 minutes of cardio",
        "completed": False,
        "deadline": datetime(2023, 10, 11),
    },
    {
        "title": "Call mom",
        "description": "Catch up with mom over the phone",
        "completed": True,
        "deadline": datetime(2023, 10, 12),
    },
    {
        "title": "Clean the house",
        "description": "Vacuum and dust all rooms",
        "completed": False,
        "deadline": datetime(2023, 10, 13),
    },
    {
        "title": "Pay bills",
        "description": "Pay electricity and internet bills",
        "completed": True,
        "deadline": datetime(2023, 10, 14),
    },
    {
        "title": "Write blog post",
        "description": "Draft a new blog post on Django",
        "completed": False,
        "deadline": datetime(2023, 10, 16),
    },
    {
        "title": "Plan vacation",
        "description": "Research destinations and book flights",
        "completed": False,
        "deadline": datetime(2023, 10, 17),
    },
    {
        "title": "Attend meeting",
        "description": "Project meeting at 3 PM",
        "completed": True,
        "deadline": datetime(2023, 10, 18),
    },
    {
        "title": "Cook dinner",
        "description": "Prepare a healthy meal",
        "completed": False,
        "deadline": datetime(2023, 10, 19),
    },
]


# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the products index.")
    return render(request, "index.html", {"title": "Super Home Page", "tasks": tasks})


def details(request):
    return HttpResponse(
        """<h1>Product Details</h1> 
        <hr> 
        <p>Product details page</p>"""
    )
