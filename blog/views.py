from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Member, Category
from django.core.paginator import Paginator
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def members(request):
   
    # context = {"articles": Member.objects.all()}
    # context = {"articles": Member.objects.filter(status= "P").order_by("-created_at"),
    article_list = Member.objects.published().order_by("-created_at")
    paginator = Paginator(article_list, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = { "articles": page_obj ,
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


def category(request, slug):
    categories = get_object_or_404(Category, status=True, slug = slug)
    category_post = categories.articles.published()
    paginator = Paginator(category_post, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"categories": page_obj,
    # context = {"categories": get_object_or_404(Category,status=True, slug = slug )
    # Category.objects.filter(status=True, slug = slug),if we use this, we need two loops in the tamplate files(category.html)
    } 
    return render(request, "blog/category.html", context) 