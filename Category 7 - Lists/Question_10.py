# remove all occurrence of 20 from the list

list = [5, 20, 15, 20, 25, 50, 20]
counter = 0
counter2 = list.count(20)
while counter < counter2:
    list.remove(20)
    counter += 1
print(list)


'''
Muslim solution:
list = [5, 20, 15, 20, 25, 50, 20]


def remove_value(sample_list, val):
    return [value for value in sample_list if value != val]


result_list = remove_value(list, 20)
print(result_list)


'''