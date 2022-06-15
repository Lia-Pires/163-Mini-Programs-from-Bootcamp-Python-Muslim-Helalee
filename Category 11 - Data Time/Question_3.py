# Subtract a week (7 days)  from a given date.s

# given_date = datetime(2100, 2, 25)

from datetime import datetime, timedelta

date = datetime(2100, 2, 25)

new_date = date - timedelta(7)

print(new_date)

'''
Muslim solution:
from datetime import datetime, timedelta

given_date = datetime(2100, 2, 25)
daya_to_subtract = 7

resulting_date = given_date - timedelta(days=daya_to_subtract)

print(resulting_date)

'''