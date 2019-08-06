from django.shortcuts import render, get_object_or_404, reverse
from django.http import Http404, HttpResponseRedirect
from .models import *
# Create your views here.


def index(request):
    questions = Question.objects.all().filter(publish=True).order_by('-date')
    return render(request, 'polls/index.html', {
        'questions': questions,
        })


def q_page(request, id):
    question = get_object_or_404(Question, pk=id)
    if question.publish:
        return render(request, 'polls/q_page.html', {'question': question})
    else:
        return render(request, 'polls/404.html')


def vote(request, id):
    q = get_object_or_404(Question, pk=id)
    try:
        if q.choice.date_limit_checker() == 1:
            if request.POST['vote'] == 'plus':
                    q.choice.p_votes += 1
            elif request.POST['vote'] == 'minus':
                    q.choice.n_votes += 1
            else:
                return render(request, 'polls/q_page.html', {
                    'question': q,
                    'error': 'خطایی رخ داده!',
                })
        elif q.choice.date_limit_checker() == 0:
            return render(request, 'polls/q_page.html', {
                    'question': q,
                    'error': 'این نظر سنجی دارای محدودیت زمانی است و هنوز شروع نشده!',
                })
        elif q.choice.date_limit_checker() == 2:
            return render(request, 'polls/q_page.html', {
                    'question': q,
                    'error': 'این نظرسنجی دارای محدودیت زمانی بوده و مهلت آن به اتمام رسیده است.',
                })
        else:
            return HttpResponseRedirect(reverse('polls:q_page', args=[id]))
    except:
        return render(request, 'polls/q_page.html', {
            'question': q,
            'error': 'خطایی رخ داده!',
        })
    else:
        q.choice.save()
        return HttpResponseRedirect(reverse('polls:q_page', args=[id]))
