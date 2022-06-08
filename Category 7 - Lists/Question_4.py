# Concatenate two lists in the following order


list1 = ["Hello ", "Hi "]
list2 = ["Dear", "Sir"]

# ['Hello Dear', 'Hello Sir', 'Hi Dear', 'Hi Sir']

list3 = []

for i in list1:
    for j in list2:
        list3.append(i + j)

print(list3)


'''
Muslim solution
list1 = ["Hello ", "Hi "]
list2 = ["Dear", "Sir"]

result = [x + y for x in list1 for y in list2]
print(result)

'''

