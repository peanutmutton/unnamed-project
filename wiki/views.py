from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Article, ArticleContent

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_create.html"
    fields = "__all__"

class ArticleContentCreateView(CreateView):
    model = ArticleContent
    template_name = "article_content_create.html"
    fields = "__all__"