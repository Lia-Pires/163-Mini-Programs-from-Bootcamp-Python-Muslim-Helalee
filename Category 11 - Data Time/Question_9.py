# Calculate the date 4 months from the given date


# given_date = datetime(2035, 5, 20).date()



'''
Muslim solution:
from datetime import datetime

from dateutil.relativedelta import relativedelta

given_date = datetime(2035, 5, 20).date()

months_to_add = 4

new_date = given_date + relativedelta(months=months_to_add)

print(new_date)

'''
