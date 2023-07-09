from django.http import Http404
from django.shortcuts import get_object_or_404
from blog.models import Member
class FieldMixin(object):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if  request.user.is_superuser:
            self.fields= ["title",
                    "description",
                    "slug",
                    "category",
                    "author",
                    "status",
                    "photo",]
        elif request.user.is_author:
            self.fields= ["title",
                    "description",
                    "slug",
                    "category",
                    "photo",]
        else:
            raise Http404("you must be logged in")


        return super().dispatch(request, *args, **kwargs)

class FormValidMixin(object):
    def form_valid(self, form):
        if not self.request.user.is_superuser:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            self.obj.status = "D"
            self.obj.save()
        return super().form_valid(form)



class AccessMixin(object):
    def dispatch(self, request,pk, *args, **kwargs):
        articles = get_object_or_404(Member, pk=pk)
        if  request.user.is_superuser or (articles.status in ["D", "B"] and articles.author == request.user) :
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما اجازه دسترسی به این صفحه را ندارید")


class DeleteMixin(object):
    def dispatch(self, request,pk, *args, **kwargs):
        articles = get_object_or_404(Member, pk=pk)
        if  request.user.is_superuser or (articles.status in ["D", "B"] and articles.author == request.user) :
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما دسترسی به این صفحه را ندارید")