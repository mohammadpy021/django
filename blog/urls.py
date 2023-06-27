from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("members/", views.members, name="members"),
    path("members/<slug:slug>/", views.detail, name="detail")
] 

