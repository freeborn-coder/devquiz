from django.contrib import admin
from .models import Question, QuizCategory, Score, User

# Register your models here.

admin.site.register(QuizCategory)
admin.site.register(Question)
admin.site.register(Score)
admin.site.register(User)