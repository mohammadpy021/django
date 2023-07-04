from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Member



class HomeList(LoginRequiredMixin, ListView):
    queryset = Member.objects.all()
    template_name = "registration/home.html"
