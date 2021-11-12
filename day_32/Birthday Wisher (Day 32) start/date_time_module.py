import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1995, month=12, day=24, hour=4, minute=42, second=1)
print(date_of_birth)
