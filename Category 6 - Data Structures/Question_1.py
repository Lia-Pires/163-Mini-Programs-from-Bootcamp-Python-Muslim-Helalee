# Given two lists create a third list by picking odd-index elements from the first list and even-index elements from the second.

list_one = [3, 6, 9, 12, 15, 18, 21]
list_two = [4, 8, 12, 16, 20, 24, 28]
list_3 = []

for i in list_one:
    if i % 2 != 0:
        list_3.append(i)
for j in list_two:
    if j % 2 == 0:
        list_3.append(j)
print(list_3)

'''Muslim solution:

list_one = [3, 6, 9, 12, 15, 18, 21]
list_two = [4, 8, 12, 16, 20, 24, 28]

list_three = list()

odd_elements = list_one[1::2]
print(odd_elements)

even_elements = list_two[0::2]
print(even_elements)


list_three.extend(odd_elements)
list_three.extend(even_elements)
print(list_three)

'''

