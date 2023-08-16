import datetime

print('Hello FRED')

def CalculateDayBetweenDates(beginDate, endDate):
    return (endDate - beginDate).days

delay = CalculateDayBetweenDates(datetime.date(2017, 12, 28), datetime.date(2018, 1, 1))

for i in reversed(range(delay)):
    print(datetime.date(2017, 12, 28) + datetime.timedelta(days=i))

print('Goodbye FRED')