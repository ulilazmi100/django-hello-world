from django.urls import path
from . import views

urlpatterns = [
    path("", views.page_landing),
    path("about", views.page_about)
]