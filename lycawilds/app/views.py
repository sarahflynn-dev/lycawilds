from django.shortcuts import render, redirect, HttpResponse
from .models import TodoItem
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def todos(request):
    items = TodoItem.objects.all()
    return render(request, 'todos.html', {"todos": items})

def news(request):
    return render(request, 'news.html')

def guide(request):
    return render(request, 'fieldguide.html')

def browse(request):
    return render(request, 'browse.html')

@login_required
def dashboard(request):
    return render(request, "dashboard.html")
