# Return a set of all the unique elements in sets A & B

set_one = {10, 20, 30, 40, 50}
set_two = {30, 40, 50, 60, 70}

new_set = set_one.symmetric_difference(set_two)
print(new_set)

'''
Muslim solution:
set_one = {10, 20, 30, 40, 50}
set_two = {30, 40, 50, 60, 70}

print(set_one.symmetric_difference(set_two))

'''