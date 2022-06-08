# Given a Python list of numbers. Turn every item of a list into its square

list = [1, 2, 3, 4, 5, 6, 7]
squared_list = []

for i in list:
    squared_list.append(i ** 2)

print(squared_list)    


'''
Muslim solution:

list = [1, 2, 3, 4, 5, 6, 7]

list = [x * x for x in list]

print(list)

'''