# Reverse the following list using for loop

list = [10, 20, 30, 40, 50]
new_list = []

N = len(list) - 1

for number in range(N + 1):
    new_list.append(list[N])
    N -= 1

print(new_list)


'''
Muslim solution:
list = [10, 20, 30, 40, 50]

start = len(list) - 1
stop = -1
step = -1

for i in range(start, stop, step):
    print(list[i])

'''