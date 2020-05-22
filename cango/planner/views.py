from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'planner/main.html', context)


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
