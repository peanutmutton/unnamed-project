from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from simple_history.models import HistoricalRecords

User = get_user_model()
class Article(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.RESTRICT)
    content = RichTextUploadingField(blank=True, null=True)
    history = HistoricalRecords()
    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("special_status", "Can create articles"),
        ]

    def get_absolute_url(self):
        return reverse("article_detail", args=[self.slug])


#
# class ArticleContent(models.Model):
#     date_edited = models.DateTimeField(auto_now=True)
#     content = RichTextField(blank=True, null=True)
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     editor = models.ForeignKey(User, on_delete=models.RESTRICT)
#
#     def __str__(self):
#         return self.article.title + str(self.date_edited)

