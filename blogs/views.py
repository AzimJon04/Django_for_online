from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView,  UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogModel


# Create your views here.
def HomePages(request):
    return render(request, 'blogs/home_page.html')


class ListBlog(ListView):
    model = BlogModel
    template_name = 'blogs/blog_list.html'
    context_object_name = 'blogs'


class DetailBlog(DetailView):
    model = BlogModel
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'blog'


class BlogCreate(CreateView):
    model = BlogModel
    template_name = 'blogs/blog_create.html'
    fields = ['title', 'description', 'author']


class BlogUpdate(UpdateView):
    model = BlogModel
    template_name = 'blogs/blog_update.html'
    fields = ['title', 'description']

class BlogDelete(DeleteView):
    model = BlogModel
    template_name = 'blogs/blog_delete.html'
    success_url = reverse_lazy('list_blog')