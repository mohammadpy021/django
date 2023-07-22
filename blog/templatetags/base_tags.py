from django import template
from ..models import Category, Settings, Category, Member
from django.db.models import Count, Q
from datetime import datetime , timedelta
register = template.Library()



@register.simple_tag()
def title():
    name =  Settings.objects.all().first() if Settings.objects.all() else "سایت جنگو"
    return name


@register.inclusion_tag("blog/partial/navbar.html")
def navbar():#use {%navbar%} in templates
    return {
        "categories": Category.objects.filter(status= True)
    }
@register.inclusion_tag("blog/partial/popular_articles.html")
def popular_articles():#use {%navbar%} in templates
    last_month = datetime.today() - timedelta(days=30)
    return {
        "popular_articles": Member.objects.published()\
        .annotate(count=Count('hits',filter=Q(articlehit__created__gt = last_month))).order_by('-count')[:5]
    }
@register.inclusion_tag("registration/partial/link.html")
def link(request, link_name, content, classes):
    return {
        "request": request,
        "link_name": link_name,
        "link" : f"accounts:{link_name}",
        "content": content,
        "classes" : classes
    }

