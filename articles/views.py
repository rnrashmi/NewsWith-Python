from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from .models import Article
from django.urls import reverse_lazy


# Create article
class ArticlaCreateView(CreateView):
    model=Article
    template_name='article_create.html'
    fields=('title','body','author',)
    
#List articles
class ArticleListView(ListView):
    model=Article
    template_name='article_list.html'

class ArticleDetailsView(DetailView):
    model=Article
    template_name='article_detail.html'

class ArticleUpdateView(UpdateView):
    model=Article
    fields=('title','body',)
    template_name='article_edit.html'

class ArticleDeleteView(DeleteView):
    model=Article
    template_name='article_delete.html'
    success_url=reverse_lazy('article_list')
