from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Member, Category, User
from django.core.paginator import Paginator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# def members(request):
   
    
    
#     article_list = Member.objects.published().order_by("-created_at")
#     paginator = Paginator(article_list, 2)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     context = { "articles": page_obj ,
#     }

#return render(request, "blog/index.html", context)
class ArticleListView(ListView):
    # model = Member
    queryset = Member.objects.published()
    paginate_by = 3 
    # template_name = "blog/index.html"
    # context_object_name = "articles"



# def detail(request, slug):
#     # context = {"article":Member.objects.get(slug= slug)}
#     context = {"article":get_object_or_404(Member, slug=slug, status="P"),
#     } 
#     # template = loader.get_template("detail.html")
#     # return HttpResponse(template.render(context, request))
#     return render(request, "blog/post.html", context) 
class ArticleDeatil(DetailView):
    # template_name = "blog/post.html"
    # context_object_name = "article"
    def get_object(self):
        self.slug = self.kwargs["slug"]
        # return get_object_or_404(Member, slug=self.slug, status="P")
        return Member.objects.get(slug= self.slug)

# def category(request, slug):
#     categories = get_object_or_404(Category, status=True, slug = slug)
#     category_post = categories.articles.published()
#     paginator = Paginator(category_post, 2)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     context = {"categories": page_obj,
#     # context = {"categories": get_object_or_404(Category,status=True, slug = slug )
#     # Category.objects.filter(status=True, slug = slug),if we use this, we need two loops in the tamplate files(category.html)
#     } 
#     return render(request, "blog/category.html", context) 


class CategoryView(ListView):
    paginate_by = 3 
    # context_object_name = "categories"
    template_name = "blog/category.html"
    def get_queryset(self):
        
        self.slug = self.kwargs["slug"]
        category = get_object_or_404(Category, status=True, slug = self.slug)#Category.objects.all() won't work we need only one object
        return category.articles.published()

class AuthorView(ListView):
    paginate_by = 3 
    template_name = "blog/author_list.html"
    def get_queryset(self):
        global author
        self.author = self.kwargs["author"]
        author = get_object_or_404(User,  username = self.author)
        return author.articles.published()
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["author"] =  author
    #     return context
    
    
    