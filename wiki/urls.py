from django.urls import path
from .views import ArticleDetailView, ArticleListView, ArticleCreateView, ArticleContentCreateView

urlpatterns = [

    path("", ArticleListView.as_view(), name="article_list"),
    path("startarticle/", ArticleCreateView.as_view(), name="article_start"),

    path("edit/", ArticleContentCreateView.as_view(), name="article_edit"),
    # Make it like this >>> path("<slug:slug>/edit/", name="article_edit")
    # path("articlecontentcreate/", ArticleContentCreateView.as_view(), name="article_content_create"),
    path("<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),


]