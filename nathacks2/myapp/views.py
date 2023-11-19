from django.shortcuts import render
from .models import Item
from django.shortcuts import redirect

def home(request):
    items = Item.objects.all()
    return render(request, 'myapp/home.html', {'items': items})

def webcam_view(request):
    return render(request, 'myapp/webcam.html')