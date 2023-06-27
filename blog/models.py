from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from extensions.utils import jalali_convertor


class Category(models.Model):
    title= models.CharField(max_length=255, verbose_name=_("عنوان"))
    slug = models.SlugField(max_length=255, unique=True, default='', help_text=("آدرس slug"),verbose_name=_("نامک")) 
    position = models.IntegerField(verbose_name=_("پوزیشن"), default=1) 
    status = models.BooleanField(default=True, verbose_name=_("نمایش داده شود"))
    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته بندی ها"
    def __str__(self):
        return self.title
    

class Member(models.Model):
    STATUS = [
        ("P", "انتشار"),
        ("D", "پیش نویس"),
    ]
    title= models.CharField(max_length=255, verbose_name=_("عنوان"))
    description = models.TextField(blank=True, null=True, verbose_name=_("توضیحات"))
    slug = models.SlugField(max_length=255, unique=True, default='', help_text=("آدرس slug"),verbose_name=_("نامک")) 
    category = models.ManyToManyField(Category, verbose_name="دسته بندی ها", related_name='members')
    # created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاریخ انتشار"))
    # updated_at = models.DateTimeField(auto_now=True)
    created_at = jmodels.jDateTimeField(auto_now_add=True, verbose_name=_("تاریخ انتشار"))
    updated_at = jmodels.jDateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS, verbose_name=_("وضعیت"))
    photo = models.ImageField(upload_to="photo/", verbose_name=_("تصاویر"))
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقاله ها "



class Settings(models.Model):
    title= models.CharField(max_length=255, verbose_name=_("عنوان سایت "), help_text="عنوان سایت در قسمت navbar")
    class Meta:
        verbose_name = "عنوان سایت"
        verbose_name_plural = "عنوان سایت"
    def __str__(self):
        return self.title
