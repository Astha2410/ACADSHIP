from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("index/", views.index, name = "index"),
    path("contact/", views.contact_view, name="contact"),
    path("about/", views.about, name="about"),
    path("filter/", views.category, name="filter")
]