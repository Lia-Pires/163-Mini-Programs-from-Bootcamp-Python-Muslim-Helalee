# find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

list = [5, 10, 15, 20, 25, 50, 20]

list[list.index(20)] = 200
print(list)


'''
Muslim solution:
list = [5, 10, 15, 20, 25, 50, 20]

index = list.index(20)
list[index] = 200

print(list)


'''