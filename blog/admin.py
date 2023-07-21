from django.contrib import admin, messages
from django.db import models
from .models import Member, Category, Settings, IPAddress
from django.utils.html import format_html
@admin.action(description="تغییر حالت به انتشار")
def make_published(modeladmin, request, queryset):
    updated  = queryset.update(status= "P")
    modeladmin.message_user(
            request,
                f"{updated} مقاله منتشر شد.",
                
        )
@admin.action(description="تغییر حالت به پیش نویس")
def make_draft(modeladmin, request, queryset):
    updated = queryset.update(status="D")
    modeladmin.message_user(
            request,
                f"{updated} مقاله پیش نویس شد.",
                
        )

@admin.action(description="قابل نمایش")
def make_active(modeladmin, request, queryset):
    updated  = queryset.update(status=True)
    modeladmin.message_user(
            request,
                f"{updated} دسته بندی فعال شد.",
                
        )
@admin.action(description="غیر قابل نمایش")
def make_deactive(modeladmin, request, queryset):
    updated = queryset.update(status=False)
    modeladmin.message_user(
            request,
                f"{updated} دسته بندی غیرفعال شد.",
                
        )

class Category_Admin(admin.ModelAdmin):
   
    list_display = ['position', 'title', 'slug', 'parent', 'status' ]
    list_filter = ["status"]
    search_fields = ["title" ]
    actions = [make_active, make_deactive]
    prepopulated_fields = {"slug": ("title",)}
    # ordering = ["parent", "position"] we can use ordeing either here or in modles in class  Meta:
    #  list_filter = [
    #     ("status", admin.BooleanFieldListFilter),
    # ]



admin.site.register(Category, Category_Admin)


class Admin(admin.ModelAdmin):
   
    list_display = ['title', 'status','slug', 'author', 'thumbnail', 'get_categories']
    list_filter = ["status", "created_at"]
    search_fields = ["title", "description", ]
    actions = [make_published, make_draft]
    prepopulated_fields = {"slug": ("title",)}
    #  list_filter = [
    #     ("status", admin.BooleanFieldListFilter),
    # ]
    # def get_categories(self, obj):
    #     return  ",".join([i.title for i in obj.category.filter(status=True)])
    # get_categories.short_description = "دسته بندی ها"
    def thumbnail(self, obj):
        return format_html('<img src="{}" style="width: 130px; \
        height: 100px;border-radius: 10px;"/>'.format(obj.photo.url))






admin.site.register(Member, Admin)
admin.site.register(IPAddress) 
admin.site.register(Settings) 
# admin.site.site_header  =  "سایت جنگو ما"  