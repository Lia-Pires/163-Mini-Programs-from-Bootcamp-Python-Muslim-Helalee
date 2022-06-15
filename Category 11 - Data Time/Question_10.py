# Calculate number of days between two given dates


# date_1 = datetime(2050, 2, 25)

# date_2 = datetime(2065, 9, 17)


from datetime import datetime

date_1 = datetime(2050, 2, 25)
date_2 = datetime(2065, 9, 17)
days_between = None

days_between = date_2 - date_1

print("Number of Days:", days_between.days)


'''
Muslim solution:

from datetime import datetime

date_1 = datetime(2050, 2, 25)
date_2 = datetime(2065, 9, 17)
delta = None

if date_1 > date_2:
    print("Date 1 is greater")
    delta = date_1 - date_2
else:
    print("Date 2 is greater")
    delta = date_2 - date_1

print("Number of Days:", delta.days)

'''