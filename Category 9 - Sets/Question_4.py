# Given two sets, update the first set with items that exist only in the first set and not in the second set.

set_one = {10, 20, 30}
set_two = {20, 40, 50}

set_one.difference_update(set_two)
print(set_one)


'''
Muslim solution:
set_one = {10, 20, 30}
set_two = {20, 40, 50}

set_one.difference_update(set_two)
print(set_one)

'''