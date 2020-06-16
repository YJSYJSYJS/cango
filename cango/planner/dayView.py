from django.shortcuts import render

import datetime

from .models import Post


def day_view(request):
    # 일단 오늘 확인
    today = str(datetime.date.today())

    # 오늘 일정 가져오기
    # 시작날짜가 오늘보다 이전이고, 종료날짜가 오늘 이후
    # posts = Post.objects.filter(start_date__lte=today, end_date__gte=today)
    posts = Post.objects.filter(start_date__contains=today, end_date__contains=today)

    # 보낼거: 일정 제목, 시작시간, 종료시간
    events = []
    for post in posts:
        title = post.title
        str_time = str(post.start_date).split(" ")[1].split(':')[0]
        end_time = str(post.end_date).split(" ")[1].split(':')[0]
        events.append(Event(title, str_time, end_time))

    context = {'events': events}
    return render(request, 'planner/day.html', context)


class Event(object):
    def __init__(self, title, str_time, end_time):
        self.title = title
        self.str_time = str_time
        self.end_time = end_time
        return


