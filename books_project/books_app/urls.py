from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /books/
    url(r'^index/', views.index, name='index'),
    url(r'^books/', views.books, name='books'),
]
