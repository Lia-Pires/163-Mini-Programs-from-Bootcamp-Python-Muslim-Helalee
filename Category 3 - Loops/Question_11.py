# Write a program to display all prime numbers within a range

def print_range(number, number_2):
    for N in range(number, number_2, 1):
        print(N)


print_range(15, 50)


''' 
Muslim solution:
start = 1
end = 50

print(f"Prime Number between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                break

        else:
            print(num)

'''