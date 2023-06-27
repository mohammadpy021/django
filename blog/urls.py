from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.members, name="members"),
    path("members/<slug:slug>/", views.detail, name="detail"),
    path("category/", views.category, name="category"),
] 

