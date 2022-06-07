# Given a list, remove the element at index 4 and add it to the 2nd position and at the end of the list

list = [34, 54, 67, 89, 11, 43, 94]
item = list[4]
del(list[4])
list.insert(2, item)
list.append(item)

print(list)


'''Muslim solution:

list = [34, 54, 67, 89, 11, 43, 94]

target_element = list.pop(4)
print(list)

list.insert(2, target_element)
print(list)


list.append(target_element)
print(list)
'''