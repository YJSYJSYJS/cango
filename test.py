import datetime

days = []
# 오늘 날짜
today = datetime.date.today()

# 요일 of today
t_week = today.weekday()

for i in range(-1, 6):
    weekday = today + datetime.timedelta(i-t_week)
    week_str = weekday.strftime("%A(%m-%d)")
    print(week_str)
    days.append(week_str)


print(days)
