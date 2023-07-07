from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Member
from django.urls import reverse


class HomeList(LoginRequiredMixin, ListView):
    template_name = "registration/home.html"
    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Member.objects.all()
        else:
            queryset = Member.objects.filter(author= self.request.user)
    
        return queryset 


class ArticleCreate(LoginRequiredMixin, CreateView):
    template_name = "registration/article-create-update.html"
    model = Member
    fields = ["title",
"description",
"slug",
"category",
"author",
"status",
"photo",]
    # def get_success_url(self):
    #     return reverse('accounts:home')

