from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Article

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"
