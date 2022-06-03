# Use a loop to display elements from the given list that are present at even index positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for N in my_list:
    if my_list.index(N) % 2 == 0:
        print(N)  


'''
Muslim solution
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in my_list[1::2]:
    print(i, end=" ")

'''