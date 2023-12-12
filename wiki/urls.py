from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (ArticleDetailView,
                    ArticleListView,
                    ArticleCreateView,
                    ArticleUpdateView,
                    ArticleVersionView,
                    )


urlpatterns = [

    path("", ArticleListView.as_view(), name="article_list"),
    path("startarticle/", ArticleCreateView.as_view(), name="article_start"),
    path("<slug:slug>/", ArticleDetailView.as_view(), name="article_detail"),
    path("<slug:slug>/edit/", ArticleUpdateView.as_view(), name="article_edit" ),
    path("<slug:slug>/versions/", ArticleVersionView.as_view(), name="article_versions"),
    # path("edit/", ArticleContentCreateView.as_view(), name="article_edit"),
    # Make it like this >>> path("<slug:slug>/edit/", name="article_edit")
    # path("articlecontentcreate/", ArticleContentCreateView.as_view(), name="article_content_create"),
]

