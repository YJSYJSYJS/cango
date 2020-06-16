from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import calView
from . import ttView
from .models import Post

from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.hashers import make_password

from register.models import Puser

def todo(request):
    posts = Post.objects.all().order_by('end_date')
    # context = {'posts': posts}
    context = {'posts': posts}
    return render(request, 'planner/todo.html', context)


def view_month(request):
    # posts = Post.objects.all()
    # context = {'posts': posts}
    # cal_html = calendar.HTMLCalendar(firstweekday=0)
    # context = {'cal_html': cal_html.formatmonth(2020, 6)}
    # return render(request, 'planner/month.html', context)
    return calView.home(request)


def view_week(request):
    # posts = Post.objects.all()
    # context = {'posts': posts}
    return ttView.tt_view(request)


def day(request):
    user_id = request.session.get('user')

    if user_id:
        puser = Puser.objects.get(pk=user_id)
        account = {'user_name' : puser}
        # return HttpResponse(puser.username)
        return render(request, 'planner/day.html', account)
    # return HttpResponse('planner/day.html')

def year(request):
    return render(request, 'planner/year.html', {})


def enroll(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('todo')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'planner/enroll.html', context)
