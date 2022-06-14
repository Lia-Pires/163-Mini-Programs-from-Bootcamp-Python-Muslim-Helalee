# Print current date and time in Python
from time import gmtime, strftime
import datetime


print(datetime.datetime.now()) 


'''
Muslim solution:

from time import gmtime, strftime
import datetime

print(datetime.datetime.now())


print(datetime.datetime.now().time())

# Method 2

print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

'''