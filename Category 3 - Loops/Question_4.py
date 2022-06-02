# Print the multiplication table for a number

number = int(input("Enter a number to get it's multiplication table: "))
N = 0
result = 0

while N <= 10:
    result = N * number
    print(f"{N} x {number} = {result}")
    N += 1


'''
Muslim solution:
num = 5

for i in range(1, 11, 1):
    product = num * i
    print(product)

'''