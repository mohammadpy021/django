from django.forms import ModelForm, EmailField
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms  
class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        #start getting kwargs from views:61
        user = kwargs.pop('user')#we can also write user above:def __init__(self,user,...):
        super(ProfileForm, self).__init__(*args, **kwargs)
        #end getting kwargs from views
        if not user.is_superuser:
            self.fields['username'].disabled = True 
            self.fields['special_user'].disabled = True 
            self.fields['email'].disabled = True
            self.fields['is_author'].disabled = True
    class Meta:
        # exclude = ("first_name  ",)
        model = User
        fields = ["username",
                "first_name",
                "last_name",
                "special_user",
                "email",
                "is_author",]



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

