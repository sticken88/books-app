from django.template import RequestContext, loader
from django.shortcuts import render
from django.http import HttpResponse

from models import *

# Create your views here.
def index(request):
    #return HttpResponse("Prova pagina Django")
    template = loader.get_template('books_app/index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def books(request):

    # get the list of books
    books_list = Book.objects.order_by("title")

    template = loader.get_template('books_app/books.html')
    context = RequestContext(request, {
                                         'books_list': books_list
                                      })
    return HttpResponse(template.render(context))

