from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    questions = Question.objects.all().order_by('-date')
    return render(request, 'polls/index.html', {
        'questions': questions,
        })
