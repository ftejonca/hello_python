### Fechas ###

from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta

now = datetime.now()

def print_date(date):
    print(date.day)
    print(date.month)
    print(date.year)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
    
print_date(now)

year_2025 = datetime(2025,4, 20)

print_date(year_2025)

current_time = time(00, 30, 21)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2025, 4, 20)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(type(current_date))
print(current_date.month)

diff = year_2025 - now
print(diff)
diff = year_2025.date() - current_date
print(diff)

init_time_delta = timedelta(200,100, 100, weeks = 10)
end_time_delta = timedelta(300, 100, 100, weeks = 13)
print(end_time_delta - init_time_delta)
print(end_time_delta + init_time_delta)