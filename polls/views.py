from django.shortcuts import render, get_object_or_404, reverse
from django.http import Http404, HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


def index(request):
    questions = Question.objects.all().filter(publish=True).order_by('-date')
    return render(request, 'polls/index.html', {
        'questions': questions,
        })


def q_page(request, id):
    question = get_object_or_404(Question, pk=id)
    if question.publish:
        return render(request, 'polls/q_page.html', {
            'question': question,
            })
    else:
        return render(request, 'polls/404.html')


def pvote(request, id):
    q = get_object_or_404(Question, pk=id)
    try:
        if q.date_limit_checker() == 1:
            if request.POST:
                    q.p_votes += 1
            else:
                return render(request, 'polls/q_page.html', {
                    'question': q,
                    'error': 'خطا در ثبت رای !',
                })
        elif q.date_limit_checker() == 0:
            return render(request, 'polls/q_page.html', {
                    'question': q,
                    'error': 'این نظر سنجی دارای محدودیت زمانی است و هنوز شروع نشده!',
                })
        elif q.date_limit_checker() == 2:
            return render(request, 'polls/q_page.html', {
                    'question': q,
                    'error': 'این نظرسنجی دارای محدودیت زمانی بوده و مهلت آن به اتمام رسیده است.',
                })
        else:
            return HttpResponseRedirect(reverse('polls:q_page', args=[id]))
    except:
        return render(request, 'polls/q_page.html', {
            'question': q,
            'error': 'خطا در ثبت رای !',
        })
    else:
        q.save()
        return HttpResponseRedirect(reverse('polls:q_page', args=[id]))


def nvote(request, id):
    q = get_object_or_404(Question, pk=id)
    try:
        if q.date_limit_checker() == 1:
            if request.POST:
                    q.n_votes += 1
            else:
                return render(request, 'polls/q_page.html', {
                    'question': q,
                    'error': 'خطا در ثبت رای !',
                })
        elif q.date_limit_checker() == 0:
            return render(request, 'polls/q_page.html', {
                    'question': q,
                    'error': 'این نظر سنجی دارای محدودیت زمانی است و هنوز شروع نشده!',
                })
        elif q.date_limit_checker() == 2:
            return render(request, 'polls/q_page.html', {
                    'question': q,
                    'error': 'این نظرسنجی دارای محدودیت زمانی بوده و مهلت آن به اتمام رسیده است.',
                })
        else:
            return HttpResponseRedirect(reverse('polls:q_page', args=[id]))
    except:
        return render(request, 'polls/q_page.html', {
            'question': q,
            'error': 'خطا در ثبت رای !',
        })
    else:
        q.save()
        return HttpResponseRedirect(reverse('polls:q_page', args=[id]))


def signup(request):
    u = User()
    try:
        u.username = request.POST['username']
        u.email = request.POST['email']
        u.set_password(request.POST['password'])
        u.save()
        login(request, u)
    except:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return render(request, 'polls/profile.html', {
        'user': u,
    })


def signin(request):
    user_name = request.POST['username']
    passwd = request.POST['password']
    user = authenticate(request, username=user_name, password=passwd)
    if user is not None:
        login(request, user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def signout(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def profile(request):
    u = request.user
    return render(request, 'polls/profile.html', {
        'user': u,
    })


@login_required
def change_pass(request):
    u = request.user
    old_pass = request.POST['old_pass']
    new_pass = request.POST['new_pass']
    re_pass = request.POST['re_pass']
    check_pass = u.check_password(old_pass)

    def check_new_pass_eq():
        if new_pass == re_pass:
            return True
        else:
            return False

    if check_pass and new_pass == re_pass and len(new_pass) > 5:
        u.set_password(new_pass)
        u.save()
        logout(request)
        return render(request, 'polls/profile.html', {
            'user': u,
            'success': 'رمز با موفقیت تغییر یافت'
        })
    elif not u.check_password(old_pass):
        return render(request, 'polls/profile.html', {
            'user': u,
            'error': 'رمز قدیمی وارد شده نا معتبر است',
        })
    elif check_pass and new_pass == re_pass and len(new_pass) < 5:
        return render(request, 'polls/profile.html', {
            'user': u,
            'error': 'رمز وارد شده باید حداقل 5 رقم باشد',
        })
    elif check_pass and not check_new_pass_eq():
        return render(request, 'polls/profile.html', {
            'user': u,
            'error': 'رمز جدید وارد شده برابر نیست'
        })
    elif old_pass == new_pass and new_pass == re_pass:
        return render(request, 'polls/profile.html', {
            'user': u,
            'error': 'رمز جدید نباید مانند رمز قدیمی باشد'
        })

    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def user_signing(request):
    if not request.user.is_authenticated:
        return render(request, 'polls/user-signing.html')
    else:
        return HttpResponseRedirect(reverse('polls:profile'))


def comment(request, id):
    cmnt = Comments()
    try:
        cmnt.user = request.user
        cmnt.text = request.POST['comment-inp']
        cmnt.question = get_object_or_404(Question, pk=id)
        cmnt.save()
    except:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def add_q_page(request):
    u = request.user
    return render(request, 'polls/q_add.html', {
        'user': u,
    })

@login_required
def add_q(request):
    q = Question()

    try:
        q.user = request.user
        q.title = request.POST['title']
        q.text = request.POST['desc']
        if request.POST['p_text']:
            q.p_text = request.POST['p_text']
        if request.POST['n_text']:
            q.n_text = request.POST['n_text']
        if request.POST['publish']:
            q.publish = True
        else:
            q.publish = False
        q.save()
    except:
        return render(request, 'polls/q_add.html', {
            'error': 'خطا در ثبت فرم',
        })
    return HttpResponseRedirect(reverse('polls:index'))


def tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    return render(request, 'polls/tag.html', {
        'tag': tag,
    })


def tags(request):
    tags = Tag.objects.all()
    return render(request, 'polls/tags.html', {
        'tags': tags,
    })


def user_poll(request, user):
    u = get_object_or_404(User, username=user)
    return render(request, 'polls/user-poll.html', {
        'user': u,
    })


@login_required
def form_management(request):
    u = request.user
    return render(request, 'polls/form-management.html', {
        'user': u,
    })


@login_required
def delete_form(request, id):
    u = request.user
    q = get_object_or_404(Question, pk=id)
    try:
        q.delete()
    except:
        msg = 'فرآیند حذف فرم با خطا مواجه شد.'
        return render(request, 'polls/form-management.html', {
            'question': q,
            'user': u,
            'error': msg,
        })
    msg = 'فرم ' + q.title + ' با موفقیت حذف شد.'
    return render(request, 'polls/form-management.html', {
        'question': q,
        'user': u,
        'success': str(msg),
    })
