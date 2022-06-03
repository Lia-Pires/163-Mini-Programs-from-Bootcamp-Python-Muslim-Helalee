"""
Create an inner function to calculate the addition in the following way:
    Create an outer function that will accept two parameters, a and b
    Create an inner function inside the outer function that will calculate the addition of a and b
    At last, the outer function will add 5 to the addition and return it
"""


def outer(a, b):

    def inner(a, b):
        return a + b

    addition = inner(a, b)
   
    return addition + 5



result = outer(1, 2)
print(result)


''' Muslim solution:

 def outer_func(a, b):

    def inner_func(a, b):
        return a + b

    add = inner_func(a, b)

    return add + 5


result = outer_func(5, 10)
print(result) '''




