from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()
class Article(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.RESTRICT)

class ArticleContent(models.Model):
    date_modified = models.DateTimeField(auto_now=True)
    html_content = RichTextField(blank=True, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    editor = models.ForeignKey(User, on_delete=models.RESTRICT)


