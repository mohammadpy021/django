from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Member
from django.urls import reverse
from .mixins import FormValidMixin, FieldMixin, UpdateMixin


class HomeList(LoginRequiredMixin, ListView):
    template_name = "registration/home.html"
    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Member.objects.all()
        else:
            queryset = Member.objects.filter(author= self.request.user)
        return queryset 


class ArticleCreate(LoginRequiredMixin,FieldMixin, FormValidMixin, CreateView):
    template_name = "registration/article-create-update.html"
    model = Member
    # def get_success_url(self):
    #     return reverse('accounts:home')


class ArticleUpdate(LoginRequiredMixin, UpdateMixin, FieldMixin, FormValidMixin, UpdateView):
    template_name = "registration/article-create-update.html"
    model = Member


