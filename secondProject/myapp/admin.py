from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Tracking)
admin.site.register(Position)
admin.site.register(AskQA)
admin.site.register(SurveyResponse)
admin.site.register(Score)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("body",)
    list_display = ["id", "title", "images"]
    list_editable = ["title"]

admin.site.register(Author)
admin.site.register(Post, PostAdmin)

