from django import template
from ..models import Category, Settings
register = template.Library()




@register.simple_tag()
def title():
    name =  Settings.objects.all().first() if Settings.objects.all() else "سایت جنگو"
    
    return name


@register.inclusion_tag("blog/partial/navbar.html")
def navbar():
    return {
        "categories": Category.objects.filter(status= True)
    }


