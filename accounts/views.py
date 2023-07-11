from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Member
from .models import User
from .mixins import FormValidMixin, FieldMixin, AccessMixin, DeleteMixin
from .forms import ProfileForm


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


class ArticleUpdate(LoginRequiredMixin, AccessMixin, FieldMixin, FormValidMixin, UpdateView):
    template_name = "registration/article-create-update.html"
    model = Member
class ArticleDelete(DeleteMixin, DeleteView):
    model = Member
    success_url = reverse_lazy("accounts:home")
    template_name = "registration/article-delete.html"
#User
class Profile(UpdateView):
    template_name = "registration/profile.html"
    model = User
    form_class = ProfileForm
    # fields = '__all__' #when i used this the form didn't save
#     fields = ["username", # we make this fields in the forms.py,so we dont thsese anymore
# "first_name",
# "last_name",
# "special_user",
# "email",
# "is_author"]
    success_url = reverse_lazy("accounts:home")
    def get_form_kwargs(self): #sending kwargs to the form:62
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        # kwargs.update({'user': self.request.user})
        return kwargs
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
 
