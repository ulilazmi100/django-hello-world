from django.urls import path
from . import views

urlpatterns = [
    path("", views.page_landing),
    path("about", views.page_about),
    path("about/<int:id>", views.page_about),
    path("about/<int:id>/<int:year>", views.page_about),
    path("about/settings", views.page_about),
    path("all", views.page_all),
    path("picture", views.page_picture),
    path("video", views.page_video),
    path("playground", views.page_playground),
]