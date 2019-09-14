from django.shortcuts import render

# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")

def hire(request):
    """A view that displays the hire page"""
    return render(request, "hire.html")
    
def about(request):
    """A view that displays the about page"""
    return render(request, "about.html")