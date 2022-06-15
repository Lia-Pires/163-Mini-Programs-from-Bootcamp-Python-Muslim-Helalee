# Print a date in a the following format

# Day_name  Day_number  Month_name  Year

# given_date = datetime(2100, 12, 15)


from datetime import datetime


date = datetime(2100, 12, 15)

print(date.strftime("%A %d %B %Y"))


'''
Muslim solution:
from datetime import datetime


given_date = datetime(2100, 12, 15)

print(given_date.strftime("%A %d %B %Y"))

# Day_name  Day_number  Month_name  Year

'''