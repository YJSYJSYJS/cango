import datetime as dt
from datetime import date

from calendar import monthrange

from django.shortcuts import render
from django.utils.safestring import mark_safe

from .models import ContestEvent
from .models import Post


from .Calender import ContestCalendar


def named_month(pMonthNumber):
    # 그냥 달을 숫자에서 영어로 바꿔주는거
    return date(1900, pMonthNumber, 1).strftime('%B')


def home(request):
    """
    Show calendar of events this month
    """
    # 오늘 날짜
    lToday = dt.datetime.now()
    return calendar(request, lToday.year, lToday.month)


def calendar(request, pYear, pMonth):
    """
    Show calendar of events for specified month and year
    """
    # 현재 년도
    lYear = int(pYear)
    # 요번 달
    lMonth = int(pMonth)

    # 매 달 1일
    lCalendarFromMonth = dt.datetime(lYear, lMonth, 1)
    # 매 달 마지막 날짜
    lCalendarToMonth = dt.datetime(lYear, lMonth, monthrange(lYear, lMonth)[1])

    # 해당 이벤트의 조건 필터링
    lContestEvents = Post.objects.filter(start_date__gte=lCalendarFromMonth, start_date__lte=lCalendarToMonth)

    # 사실상 여기가 전부
    lCalendar = ContestCalendar(lContestEvents).formatmonth(lYear, lMonth)

    # 이전 달 정보
    lPreviousYear = lYear
    lPreviousMonth = lMonth - 1
    if lPreviousMonth == 0:
        lPreviousMonth = 12
        lPreviousYear = lYear - 1

    # 다음 달 정보
    lNextYear = lYear
    lNextMonth = lMonth + 1
    if lNextMonth == 13:
        lNextMonth = 1
        lNextYear = lYear + 1

    # 이렇게나 많이 필요한가???? <$$$>
    context = {'Calendar': mark_safe(lCalendar), 'Month': lMonth, 'MonthName': named_month(lMonth), 'Year': lYear,
               'PreviousMonth': lPreviousMonth, 'PreviousMonthName': named_month(lPreviousMonth),
               'PreviousYear': lPreviousYear, 'NextMonth': lNextMonth, 'NextMonthName': named_month(lNextMonth),
               'NextYear': lNextYear}

    return render(request, 'planner/month2.html', context)
