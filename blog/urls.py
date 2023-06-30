from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    # path("", views.index, name="index"),
    # path("", views.members, name="members"),
    path("", views.ArticleListView.as_view(), name="members"),
    path("members/<slug:slug>/", views.detail, name="detail"),
    path("category/<slug:slug>/", views.category, name="category"),
    # path("category/<slug:slug>/<int:page>/", views.category, name="category"),
] 

