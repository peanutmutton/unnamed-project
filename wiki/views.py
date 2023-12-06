from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from .forms import ArticleForm
from .models import Article


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"


class ArticleCreateView(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        CreateView):
    model = Article
    template_name = "article_create.html"
    form_class = ArticleForm
    success_url = reverse_lazy("article_edit")
    login_url = "account_login"
    permission_required = "wiki.special_status"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.slug = slugify(self.object.title)
        self.object.save()

        return super().form_valid(form)

#Remake into a form view, as updateview doesn't create simplehistory records
class ArticleUpdateView(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        UpdateView):
    model = Article
    template_name = "article_update.html"
    form_class = ArticleForm
    # success_url = reverse_lazy("article_detail", )
    login_url = "account_login"
    permission_required = "wiki.special_status"
    # fields = ("title", "content")
    def get_success_url(self):
        return self.object.get_absolute_url()

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     print(form.cleaned_data)
    #     self.object.title = form.cleaned_data["title"]
    #     self.object.content = form.cleaned_data["content"]
    #     self.object.save()
    #     return super().form_valid(form)
        


# class ArticleContentCreateView(LoginRequiredMixin, CreateView):
#     model = ArticleContent
#     template_name = "article_content_create.html"
#     form_class = ArticleContentForm
#     login_url = "account_login"
#     # article = None
#     # def get_queryset(self):
#     #     # url_slug = self.kwargs['slug']
#     #     url_slug = self.request.GET.get('slug')
#     #     self.article = Article.objects.filter(slug=url_slug)
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.editor = self.request.user
#         # self.object.article = self.article
#         self.object.save()
#
#         return super().form_valid(form)







