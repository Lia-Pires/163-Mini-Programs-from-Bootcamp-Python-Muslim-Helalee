# Add a week (7 days) and 12 hours to a given date

# given_date = datetime(2050, 03, 15, 10, 0, 0)



from datetime import datetime, timedelta

date = datetime(2050, 3, 15, 10, 0, 0)

new_date = date + timedelta(days=7, hours=12)
print(new_date)



'''
Muslim solution:

from datetime import datetime, timedelta

given_date = datetime(2050, 3, 15, 10, 0, 0)

days_to_add = 7
resulting_date = given_date + timedelta(days=days_to_add, hours=12)
print(resulting_date)

'''
