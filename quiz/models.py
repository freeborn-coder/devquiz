from turtle import title
from django.db import models

# Create your models here.

class QuizCategory(models.Model):
    title = models.CharField(max_length=50)
    icon = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.title


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50, null=True, default=None)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField(blank=False, null=False)
    quiz_category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)


class Option(models.Model):
    text = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)


class Score(models.Model):
    correct_count = models.IntegerField()
    total_questions = models.IntegerField(default=10)
    quiz_category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)