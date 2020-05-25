from django.shortcuts import render
from .models import Post


def todo(request):
    posts = Post.objects.all()
    # context = {'posts': posts}
    context = {}
    return render(request, 'planner/todo.html', context)


def view_month(request):
    # posts = Post.objects.all()
    # context = {'posts': posts}
    context = {}
    return render(request, 'planner/month.html', context)


def view_week(request):
    # posts = Post.objects.all()
    # context = {'posts': posts}
    context = {}
    return render(request, 'planner/week.html', context)


def day(request):
    return render(request, 'planner/day.html', {})


def year(request):
    return render(request, 'planner/year.html', {})
