from django.urls import path
from .views import ArticleDetailView, ArticleListView, ArticleCreateView, ArticleContentCreateView

urlpatterns = [

    path("", ArticleListView.as_view(), name="article_list"),
    path("articlecreate/", ArticleCreateView.as_view(), name="article_create"),
    path("articlecontentcreate/", ArticleContentCreateView.as_view(), name="article_content_create"),
    path("<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),


]