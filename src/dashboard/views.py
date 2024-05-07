from django.shortcuts import render

# Create your views here.

def page_index(request):
	return render(request, "dashboard/index.html")

def page_beranda(request):
    return render(request, "dashboard/beranda.html")

def page_status(request):
    return render(request, "dashboard/status.html")

