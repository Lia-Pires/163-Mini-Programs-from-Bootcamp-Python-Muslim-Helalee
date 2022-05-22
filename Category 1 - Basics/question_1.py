# Print the result of the multiplication of two sets of integers if it is less than 1000. If the result is greater that 1000, print their sum.

from itertools import product
from tkinter import Y


def result_func(x, y):
    product = x * y

    if product < 1000:
        return product
    else:
        return x + y


result = result_func(200, 20)
print(result)




