from django import forms
from django.utils.text import slugify

from .models import Article, ArticleContent
from ckeditor.fields import RichTextFormField


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title",)
    # def clean(self):
    #     super().clean()
    #     self.cleaned_data['slug'] = slugify(self.cleaned_data['title'])




class ArticleContentForm(forms.ModelForm):

    class Meta:
        model=ArticleContent
        fields=("content", "article")
