from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Member
from jalali_date import datetime2jalali, date2jalali
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    

def members(request):
    # context = {
    #     "articles": [
    #         {"title":"this is first",
    #         "description":"this is first description"
    #         },
    #         {"title":"this is 2",
    #         "description":"this is 2 description"
    #         },
    #         {"title":"this is 3",
    #         "description":"this is 3 description"
    #         },
    #         {"title":"this is 4",
    #         "description":"this is 4 description"
    #         },
    #     ]
    # }
    # context = {"articles": Member.objects.all()}
    context = {"articles": Member.objects.filter(status= "P").order_by("-created_at")}
    # template = loader.get_template("index.html")
    # return HttpResponse(template.render(context, request))
    return render(request, "blog/index.html",context)

def detail(request, slug):
    # context = {"article":Member.objects.get(slug= slug)}
    context = {"article":get_object_or_404(Member, slug=slug, status="P")} 
    # template = loader.get_template("detail.html")
    # return HttpResponse(template.render(context, request))
    return render(request, "blog/post.html",context)
    





