# Iterate the list below, and display numbers divisible by 5, and stop the iteration when hitting a number of greater that 100 in the list


list = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for number in list:
    if number > 100:
        break
    if number % 5 == 0:
        print(number)
            



'''
Muslim solution:

for item in list:
    if (item > 100):
        break

    if (item % 5 == 0):
        print(item)

'''

