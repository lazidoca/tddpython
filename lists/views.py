from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item


def home_page(request): 
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    Item.objects.create(text=request.POST['new_item'])
    return redirect('/lists/the-only-list-in-the-world/')
