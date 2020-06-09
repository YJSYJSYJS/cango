from django.shortcuts import render

import datetime

from .models import Post


def tt_view(request):
    days = []
    # 오늘 날짜
    today = datetime.date.today()

    # 요일 of today
    t_week = today.weekday()

    # 그 주에 속한 날들 (시간표의 맨 윗줄 - 요일 표시)
    for i in range(-1, 6):
        weekday = today + datetime.timedelta(i - t_week)
        week_str = weekday.strftime("%A(%m-%d)")
        days.append(week_str)

    # 일정 가져오기
    # 필요한거: 제목, 날짜, 시작시간, 종료시간
    events = []
    posts = Post.objects.all()
    for post in posts:
        e_title = post.title
        date_str = str(post.start_date).split(" ")
        d = '-'.join(date_str[0].split('-')[1:])
        t = date_str[1].split(':')[0]
        w = datetime.datetime.strptime(date_str[0], "%Y-%m-%d").weekday()
        events.append(Event(e_title, d, t, w))

    context = {'today': today, 'days': days, 'events': events}
    return render(request, 'planner/week.html', context)


class Event(object):
    def __init__(self, title, date, time, weekday):
        self.title = title
        self.date = date
        self.time = time
        self.weekday = (weekday + 1) % 7
        return

