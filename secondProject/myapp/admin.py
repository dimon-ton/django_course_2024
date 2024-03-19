from django.contrib import admin
from .models import Tracking, Position, AskQA, SurveyResponse, Score

# Register your models here.
admin.site.register(Tracking)
admin.site.register(Position)
admin.site.register(AskQA)
admin.site.register(SurveyResponse)
admin.site.register(Score)