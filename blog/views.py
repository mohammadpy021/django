from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Member, Category
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    

def members(request):
   
    # context = {"articles": Member.objects.all()}
    context = {"articles": Member.objects.filter(status= "P").order_by("-created_at"),
    }
    # template = loader.get_template("index.html")
    # return HttpResponse(template.render(context, request))
    return render(request, "blog/index.html", context)

def detail(request, slug):
    # context = {"article":Member.objects.get(slug= slug)}
    context = {"article":get_object_or_404(Member, slug=slug, status="P"),
    } 
    # template = loader.get_template("detail.html")
    # return HttpResponse(template.render(context, request))
    return render(request, "blog/post.html", context) 


def category(request):

    context = {"category":Category.objects.all(),
    } 

    return render(request, "blog/category.html", context) 