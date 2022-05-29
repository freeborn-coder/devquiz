from atexit import register
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import View

from quiz.forms import UserForm
from .models import QuizCategory

# Create your views here.


class HomePageView(View):

    def get(self, request):
        return render(request, 'quiz/index.html', {
            'categories': QuizCategory.objects.all()
        })

    def post(self, request):
        request.session['quiz_category_id'] = request.POST.get(
            'category', None)
        user_id = request.session.get('user_id')
        next_url = 'login' if user_id == None else 'quiz'
        return HttpResponseRedirect(reverse(next_url))


class LoginView(View):
    def get(self, request):
        return render(request, 'quiz/login.html')

    def post(self, request):
        pass


class RegisterView(View):
    register_html = 'quiz/register.html'

    def get(self, request):
        user_form = UserForm()
        return render(request, self.register_html, {
            'form':user_form
        })

    def post(self, request):
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            return HttpResponseRedirect(reverse('quiz'))
        else:
            return render(request, self.register_html, {
                'form':user_form
            })


def quiz(request):
    return render(request, 'quiz/quiz-page.html')


def result(request):
    return render(request, 'quiz/result-page.html')
