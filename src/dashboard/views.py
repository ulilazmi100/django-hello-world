from django.shortcuts import render
from .queries import book_create, book_read_all, book_read_one_id, book_update, book_delete

# Create your views here.

def page_index(request):
    query = book_create()
    print (query)
    return render(request, "dashboard/index.html")

def page_beranda(request):
    return render(request, "dashboard/beranda.html")

def page_status(request):
    return render(request, "dashboard/status.html")

