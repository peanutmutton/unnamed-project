from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Article

# class ArticleAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug":["title"]}



admin.site.register(Article, SimpleHistoryAdmin)
# admin.site.register(ArticleContent)