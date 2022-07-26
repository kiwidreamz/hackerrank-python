# You are given a date. Your task is to find what the day is on that date.


# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

d,m,y = map(int,input().split())
print(list(calendar.day_name)[calendar.weekday(y,d,m)].upper())
