from django.shortcuts import render


def index_page(request):
    return render(request, 'index/index.html')


def about_page(request):
    return render(request, 'index/about.html')


def contacts_page(request):
    return render(request, 'index/contacts.html')
