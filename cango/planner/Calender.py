from datetime import date

from django.utils.html import conditional_escape as esc
from itertools import groupby
from calendar import HTMLCalendar


def day_cell(cssclass, body):
    # class 이름과 <td>에 들어갈 내용을 입력해줌
    return '<td class="%s">%s</td>' % (cssclass, body)


def group_by_day(pContestEvents):
    # 이벤트들의 날짜를 추출
    field = lambda contest: contest.start_date.day
    return dict([(day, list(items)) for day, items in groupby(pContestEvents, field)])


class ContestCalendar(HTMLCalendar):

    def __init__(self, pContestEvents):
        super(ContestCalendar, self).__init__()
        # 일요일을 첫번째로 바꿈
        self.setfirstweekday(6)
        # 이벤트들을 날짜별로 분류
        self.contest_events = group_by_day(pContestEvents)

    # 이것도 오버라이딩: day
    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            if date.today() == date(self.year, self.month, day):
                cssclass += ' today'        # today class 추가
            if day in self.contest_events:
                cssclass += ' filled'       # filled class 추가
                body = []
                for contest in self.contest_events[day]:
                    # body.append('<a href="%s">' % contest.get_absolute_url())
                    # body.append(esc(contest.contest.name))
                    body.append(contest.title)
                    body.append('</a><br/>')
                return day_cell(cssclass, '<div class="dayNumber">%d</div> %s' % (day, ''.join(body)))
            return day_cell(cssclass, '<div class="dayNumber">%d</div>' % day)
        return day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month, withyear=True):
        # 년도와 달을 주어진 것으로 바꾸고
        self.year, self.month = year, month
        # 상위 클래스의 formatmonth 함수를 호출?
        return super(ContestCalendar, self).formatmonth(year, month, withyear)
