from multiprocessing import context
from re import template
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Book
# Create your views here.
def index(request):
    t = loader.get_template('index.html')
    books = Book.objects.all().values()
    context = {
        'book' : books,
    }
    return HttpResponse(t.render(context,request))
def addbook(request):
    t = loader.get_template('addbook.html')
    return HttpResponse(t.render({},request))
def addrecord(request):
    book_id = request.POST['book_id']
    book_name = request.POST['book_name']
    book_author = request.POST['book_author']
    book_price = request.POST['book_price']
    book = Book(book_id,book_name,book_author,book_price)
    book.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request,id):
    book = Book.objects.get(id = id)
    book.delete()
    return HttpResponseRedirect(reverse('index'))
def update(request,id):
    template = loader.get_template('update.html')
    book = Book.objects.get(id =id)
    context = {
        'book' : book,
    }
    
    return HttpResponse(template.render(context,request))



def updaterecord(request):
    book_id = request.POST['book_id']
    book_name = request.POST['book_name']
    book_author = request.POST['book_author']
    book_price = request.POST['book_price']
    book = Book(book_id,book_name,book_author,book_price)
    book.save()
    return HttpResponseRedirect(reverse('index'))




