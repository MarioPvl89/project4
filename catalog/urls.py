from django.urls import path
from catalog.views import catalog_page

urlpatterns = [
    path('', catalog_page, name='catalog'),
]
