from django.shortcuts import render
from django.http import JsonResponse
from .form import UploadFileForms
import json

# Create your views here.

def agregasi(input):
    #business logic
    result = input + 1
    return result

def page_landing(request):
    # RAW JSON Body Request
    if request.method == "POST":
        print(request.POST)
        json_request = json.loads(request.body.decode("utf-8"))
        return JsonResponse({
            "message": "POST",
            "name": json_request["name"],
            "age": json_request["age"],
        })
    return render(request, "landing/index.html")

def page_all(request):
    return render(request, "landing/all.html")

def page_picture(request):
    return render(request, "landing/picture.html")

def page_video(request):
    return render(request, "landing/video.html")

def page_video(request):
    return render(request, "landing/video.html")

def page_playground(request):
    return render(request, "landing/playground.html")

def page_about(request, id: int = 0, year: int= 2024):
    name_param = ""

    # Form Data
    if request.method == "POST":
        form = UploadFileForms(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data["name"]
            file = form.cleaned_data["file"]
            print(f"name -> {name}")
            print(f"file -> {file}")
            return JsonResponse({
                "message": "POST",
                "name" : name,
            })
        else:
            return JsonResponse({
                "message": "ERROR",
            })
    # if request.method == "POST":
    #     name = request.POST.get("name", "-")
    #     file_data = request.FILES.get("file_data", None)
    #     print(file_data)
    #     return JsonResponse({
    #         "message": "POST",
    #         "name" : name
    #         })

    # URL PATH (id: int = 0, year: int= 2024) && GET REQUEST PARAM (request.GET.get)
    if request.method == "GET":
        id_param = request.GET.get("id_param", 0)
        name_param = request.GET.get("name_param", "default_name")
    if id:
        #do something
        pass
    context = {"NAME" : f"Jason {id} + {id_param}+ {name_param}", 
               "AGREGASI": agregasi(123),
               "YEAR" : year
               }
    return render(request, "landing/about.html", context)
