from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone


def todo(request):
    posts = Post.objects.all()
    # context = {'posts': posts}
    context = {'posts': posts}
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
