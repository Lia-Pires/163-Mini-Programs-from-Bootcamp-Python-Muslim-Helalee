# Given the below two lists. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order

from audioop import reverse


list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

list3 = list1 + list2
list4 = list3
list4.reverse()


print(list3, list4)


'''Muslim solution:

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

'''
