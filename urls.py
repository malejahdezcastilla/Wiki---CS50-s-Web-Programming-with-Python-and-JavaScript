from django.urls import path

from . import views


urlpatterns = [
    path("wiki", views.index, name="index"),
    path("wiki/<title>", views.entry, name="entry"),
    path("search", views.search, name= "search"),
    path("new_page", views.new_page, name="new_page"),
    path("random_page", views.random_page, name = "random_page"),
    path("edit/<title>", views.edit, name="edit") 
]
