import calendar

# MM DD YYYY
date_parts = list(map(int, input().split(' ')))
day_of_week = calendar.weekday(date_parts[2], date_parts[0], date_parts[1])

print(calendar.day_name[day_of_week].upper())
