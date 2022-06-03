# Write a function such that it can accept a variable length of argument and print all arguments value

def arguments(*args):
    for i in args:
        print (i)

arguments(2, 3, 5, "Hey", False, "Hello", "World", "Have a nice day")

'''
Muslim solution:
def func(*args):
    for i in args:
        print(i)


func(20, 10, 0, "Hey", "Are", "You", "Doing", "Well", "???")

'''