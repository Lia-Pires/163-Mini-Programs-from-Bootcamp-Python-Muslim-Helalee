# Given two list of equal size create a Python set such that it shows the element from both lists in the pair

list_one = [2, 3, 4, 5, 6, 7, 8]
list_two = [4, 9, 16, 25, 36, 49, 64]
set_one = ()


set_one = zip(list_one, list_two)
    
print(set(set_one))



'''
Muslim solution:

list_one = [2, 3, 4, 5, 6, 7, 8]
list_two = [4, 9, 16, 25, 36, 49, 64]

result = zip(list_one, list_two)
result_set = set(result)

print(result_set)

'''

