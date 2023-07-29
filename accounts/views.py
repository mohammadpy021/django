from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView
from blog.models import Member
from .models import User
from .mixins import FormValidMixin, FieldMixin, AccessMixin, DeleteMixin, AuthorsAccess
from .forms import ProfileForm, SignupForm
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
#mail confirm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


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
    # fields = ["username, firstname, ... "]
    success_url = reverse_lazy("accounts:home")
    def get_form_kwargs(self): #sending kwargs to the forms.py:61
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        # kwargs.update({'user': self.request.user})
        return kwargs
    def get_object(self):#in this case we dont need to write the pk in the urls
        return User.objects.get(pk=self.request.user.pk)



class Login(LoginView):
    def get_success_url(self):
        if not self.request.user.is_author:
            return reverse("accounts:profile")
        else:
            return reverse("accounts:home")





class Register(CreateView):
    template_name = "registration/signup.html"
    form_class = SignupForm
    # def get_success_url(self):
    #     return reverse('register_confirm')
    def form_valid(self, form):# if form.is_valid(): in non class base 
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'اکانت خود را فعال کنید.'
        message = render_to_string('registration/acctivate_account.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('<a href="/login" > لطفا ایمیل خود را تایید کنید تا ثبت نام شما کامل شود')




def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)#Auto login
        # return redirect('home')
        return HttpResponse('ایمیل شما تایید شد . اکنون میتوانید وارد شوید. <a href="/login" > ورود </a>')
    else:
        return HttpResponse('این لینک  فعال سازی منقضی شده است')
    
