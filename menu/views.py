from django.shortcuts import get_object_or_404, render

from .models import MenuItem


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def menu(request):
    menu_items = MenuItem.objects.all().order_by('name')
    return render(request, 'menu.html', {'menu_items': menu_items})


def menu_item(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)
    return render(request, 'menu_item.html', {'item': item})


def book(request):
    return render(request, 'book.html')
