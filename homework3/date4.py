import datetime
day1 = input()
day2 = input()

date_format = '%Y-%m-%d %H:%M:%S'


d1 = datetime.datetime.strptime(day1, date_format)
d2 = datetime.datetime.strptime(day2, date_format)

difference = d2 - d1

print(difference.total_seconds())