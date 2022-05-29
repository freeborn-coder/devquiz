from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='quiz.landing'),
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('quiz', views.quiz, name='quiz'),
    path('result', views.result)
]