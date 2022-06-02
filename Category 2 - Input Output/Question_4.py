# Accept a list of numbers and the size of the list as an input from the user

numbers_list = []

print("Let's make a list!")
list_size = int(input("Enter list's size: "))
for i in range(list_size):
    number = float(input(f"Enter the number at position {i}: "))
    numbers_list.append(number)

print(f"The list is: {numbers_list}")


'''
Muslim solution:

float_nums = []

list_size = int(input("Enter the list size "))

for i in range(0, list_size):
    print("Enter number at location", i, ":")

    item = float(input())
    float_nums.append(item)

print("The user list is:", float_nums)

'''