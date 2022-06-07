# Given the following two sets find the intersection and remove those elements from the first set

set1 = {65, 42, 78, 83, 23, 57, 29}
set2 = {67, 73, 43, 48, 83, 57, 29}


for item in (set1.intersection(set2)):
    set1.remove(item)

print(set1)



'''
Muslim solution:

set1 = {65, 42, 78, 83, 23, 57, 29}
set2 = {67, 73, 43, 48, 83, 57, 29}


intersection = set1.intersection(set2)
print(intersection)

for item in intersection:
    set1.remove(item)

print(set1)


'''