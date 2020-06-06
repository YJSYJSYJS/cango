import datetime as dt
from calendar import monthrange
from datetime import date
from django.shortcuts import render
from django.utils.safestring import mark_safe
from .models import ContestEvent
from .models import Post


from .Calender import ContestCalendar


def named_month(pMonthNumber):
    """
    Return the name of the month, given the month number
    """
    return date(1900, pMonthNumber, 1).strftime('%B')


def home(request):
    """
    Show calendar of events this month
    """
    lToday = dt.datetime.now()
    return calendar(request, lToday.year, lToday.month)


def calendar(request, pYear, pMonth):
    """
    Show calendar of events for specified month and year
    """
    lYear = int(pYear)
    lMonth = int(pMonth)
    lCalendarFromMonth = dt.datetime(lYear, lMonth, 1)
    lCalendarToMonth = dt.datetime(lYear, lMonth, monthrange(lYear, lMonth)[1])
    lContestEvents = ContestEvent.objects.filter(date_of_event__gte=lCalendarFromMonth, date_of_event__lte=lCalendarToMonth)
    lCalendar = ContestCalendar(lContestEvents).formatmonth(lYear, lMonth)
    lPreviousYear = lYear
    lPreviousMonth = lMonth - 1
    if lPreviousMonth == 0:
        lPreviousMonth = 12
        lPreviousYear = lYear - 1
    lNextYear = lYear
    lNextMonth = lMonth + 1
    if lNextMonth == 13:
        lNextMonth = 1
        lNextYear = lYear + 1
    lYearAfterThis = lYear + 1
    lYearBeforeThis = lYear - 1

    return render(request, 'planner/month2.html', {'Calendar': mark_safe(lCalendar),
                                                       'Month': lMonth,
                                                       'MonthName': named_month(lMonth),
                                                       'Year': lYear,
                                                       'PreviousMonth': lPreviousMonth,
                                                       'PreviousMonthName': named_month(lPreviousMonth),
                                                       'PreviousYear': lPreviousYear,
                                                       'NextMonth': lNextMonth,
                                                       'NextMonthName': named_month(lNextMonth),
                                                       'NextYear': lNextYear,
                                                       'YearBeforeThis': lYearBeforeThis,
                                                       'YearAfterThis': lYearAfterThis,
                                                   })
