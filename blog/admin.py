from django.contrib import admin
from django.db import models
from .models import Member, Category, Settings

class Category_Admin(admin.ModelAdmin):
   
    list_display = ['position', 'title', 'slug', 'parent', 'status' ]
    list_filter = ["status"]
    search_fields = ["title" ]
    prepopulated_fields = {"slug": ("title",)}
    # ordering = ["parent", "position"] we can use ordeing either here or in modles in class  Meta:
    #  list_filter = [
    #     ("status", admin.BooleanFieldListFilter),
    # ]



admin.site.register(Category, Category_Admin)
class Admin(admin.ModelAdmin):
   
    list_display = ['title', 'status','slug',  'get_categories']
    list_filter = ["status", "created_at"]
    search_fields = ["title", "description", ]
    prepopulated_fields = {"slug": ("title",)}
    #  list_filter = [
    #     ("status", admin.BooleanFieldListFilter),
    # ]
    def get_categories(self, obj):
        return  ",".join([i.title for i in obj.category.filter(status=True)])
    get_categories.short_description = "دسته بندی ها"

admin.site.register(Member, Admin)



admin.site.register(Settings)