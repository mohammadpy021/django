from django.forms import ModelForm
from .models import User

class ProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        #start getting kwargs from views:62
        user = kwargs.pop('user')#we can also write user above:def __init__(user,...):
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

