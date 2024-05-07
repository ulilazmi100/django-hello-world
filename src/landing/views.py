from django.shortcuts import render

# Create your views here.

def agregasi(input):
    #business logic
    result = input + 1
    return result

def page_landing(request):
    return render(request, "landing/index.html")

def page_about(request):
    context = {
        "NAMA" : "Jason",
        "AGREGASI": agregasi(123)
    }
    return render(request, "landing/about.html")
