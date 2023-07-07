from django.db import models
from django.contrib.auth.models import AbstractUser
from django_jalali.db import models as jmodels
from django.utils import timezone

class User(AbstractUser):
    is_author = models.BooleanField(default=False, verbose_name="وضعیت‌کاربر‌ ویژه")
    special_user = jmodels.jDateTimeField(default=timezone.now, verbose_name="کاربر ویژه تا")
    def is_special_user(self):
        if self.special_user > timezone.now():
            return True
        return False
