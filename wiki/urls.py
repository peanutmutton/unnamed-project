from django.urls import path
from .views import ArticleDetailView, ArticleListView, ArticleCreateView, ArticleUpdateView

urlpatterns = [

    path("", ArticleListView.as_view(), name="article_list"),
    path("startarticle/", ArticleCreateView.as_view(), name="article_start"),
    path("<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<slug:slug>/edit/", ArticleUpdateView.as_view(), name="article_edit" ),
    # path("edit/", ArticleContentCreateView.as_view(), name="article_edit"),
    # Make it like this >>> path("<slug:slug>/edit/", name="article_edit")
    # path("articlecontentcreate/", ArticleContentCreateView.as_view(), name="article_content_create"),



]