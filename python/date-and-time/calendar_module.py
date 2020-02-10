import calendar

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
month, day, year = map(int, input().split(" "))
print(days[calendar.weekday(year, month, day)])
