from django.urls import path
from index.views import index_page, about_page, contacts_page

urlpatterns = [
    path('', index_page, name='index'),
    path('about/', about_page, name='about'),
    path('contacts/', contacts_page, name='contacts'),
]
