#  Convert the following datetime into a string

# given_date = datetime(2035, 5, 20)


from datetime import datetime

date = datetime(2035, 5, 20)

date_string = date.strftime("%Y-%m-%d %H:%M:%S")

print(date_string)

'''
Muslim solution:

from datetime import datetime

given_date = datetime(2035, 5, 20)

string_date = given_date.strftime("%Y-%m-%d %H:%M:%S")

print(string_date)
print(type(string_date))

'''