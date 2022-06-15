# Find the day of the week of a given date

# given_date = datetime(2100, 12, 15)



from datetime import datetime

date = datetime(2100, 12, 15)

print(date.today().weekday())

print(date.strftime("%A"))


'''
Muslim solution:

from datetime import datetime

given_date = datetime(2100, 12, 15)

print(given_date.today().weekday())

print(given_date.strftime("%A"))

'''
