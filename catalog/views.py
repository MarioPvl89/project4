from django.shortcuts import render
from .models import Car

def catalog_page(request):
    cars = Car.objects.all()
    return render(request, 'catalog/catalog.html', {'cars': cars})
