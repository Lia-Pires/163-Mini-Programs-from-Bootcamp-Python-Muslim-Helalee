# Given two list of numbers, create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list

list1 = [10, 20, 23, 11, 17, 44, 55]
list2 = [13, 43, 24, 36, 12, 33, 66]
new_list = []

for number in list1:
    if number % 2 != 0:
        new_list.append(number)
for number in list2:
    if number % 2 != 0:
        new_list.append(number)

print(new_list)



'''Muslim Solution:
    def merge_list(list_one, list_two):
    list_three = []

    for num in list_one:
        if (num % 2 != 0):
            list_three.append(num)

    for num in list_two:
        if (num % 2 == 0):
            list_three.append(num)

    return list_three


list1 = [10, 20, 23, 11, 17, 44, 55]
list2 = [13, 43, 24, 36, 12, 33, 66]

print(merge_list(list1, list2))

'''