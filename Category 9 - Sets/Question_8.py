# Update set1 by adding items from set2, except common items


set_one = {10, 20, 30, 40, 50}
set_two = {30, 40, 50, 60, 70}

set_one.update(set_two)
print(set_one)


'''
Muslim solution:
set_one = {10, 20, 30, 40, 50}
set_two = {30, 40, 50, 60, 70}

set_one.symmetric_difference_update(set_two)

print(set_one)

'''