from django.urls import path

# needed for views.index below
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]