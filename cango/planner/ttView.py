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
    posts = Post.objects.all().order_by('end_date')

    context = {'today': today, 'days': days, 'posts': posts}
    return render(request, 'planner/week.html', context)
