# Accept number from user and calculate the sum of all number from 1 to the given number

number = int(input("Enter a number: "))
sum = 0
counter = 0

while counter <= number:
    sum += counter
    counter += 1
print(f"The sum from 1 to {number} is {sum}")


'''
Muslim solution:
sum = 0

num = int(input("Enter a number "))

for i in range(1, num + 1, 1):
    sum += i

print("The sum is:", sum)

'''
