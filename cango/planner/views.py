from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'planner/post_list.html', context)

def day(request):
    return render(request, 'planner/day.html', )

def year(request):
    return render(request, 'planner/year.html', )