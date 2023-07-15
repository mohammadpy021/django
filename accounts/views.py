from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView
from blog.models import Member
from .models import User
from .mixins import FormValidMixin, FieldMixin, AccessMixin, DeleteMixin, AuthorsAccess
from .forms import ProfileForm
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin



class HomeList(LoginRequiredMixin,AuthorsAccess, ListView):
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



class ArticleUpdate(LoginRequiredMixin,SuccessMessageMixin, AccessMixin, FieldMixin, FormValidMixin, UpdateView):
    template_name = "registration/article-create-update.html"
    model = Member
    success_message = "محتوا با موفقیت آپدیت شد."
class ArticleDelete(DeleteMixin, DeleteView):
    model = Member
    success_url = reverse_lazy("accounts:home")
    template_name = "registration/article-delete.html"
#User
class Profile(LoginRequiredMixin, UpdateView):
    template_name = "registration/profile.html"
    model = User
    form_class = ProfileForm
    # fields = '__all__' #when i used this the form didn't save
    # fields = ["..."]
    success_url = reverse_lazy("accounts:home")
    def get_form_kwargs(self): #sending kwargs to the forms.py:61
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        # kwargs.update({'user': self.request.user})
        return kwargs
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)



class Login(LoginView):
    def get_success_url(self):
        if not self.request.user.is_author:
            return reverse("accounts:profile")
        else:
            return reverse("accounts:home")





        

 
