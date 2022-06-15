# Convert string into a datetime object
from datetime import datetime


date_string = "Feb 25 2300 4:20PM"
new_date = datetime.strptime(date_string, "%b %d %Y %I:%M%p")

print(new_date)



'''
Muslim solution:
from datetime import datetime


date_string = "Feb 25 2300 4:20PM"
datetime_obj = datetime.strptime(date_string, "%b %d %Y %I:%M%p")

print(datetime_obj)

'''