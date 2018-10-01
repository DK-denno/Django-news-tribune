from django.contrib import admin
from .models import Editor,tags,Article,NewsLetterRecipients
# Register your models here.



class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal=('tags',)

admin.site.register(Editor)
admin.site.register(tags)
admin.site.register(Article,ArticleAdmin)
admin.site.register(NewsLetterRecipients)