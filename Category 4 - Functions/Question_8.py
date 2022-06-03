# Generate a Python list of all the even numbers between 4 to 30

def even_list(a, b):
    list = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            list.append(i)
    print(list)


even_list(4, 30)



'''
Muslim solution:

print(list(range(4, 30, 2)))

'''