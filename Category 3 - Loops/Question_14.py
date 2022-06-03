# Display the cube of the number up to a given integer

def nums_cube(number):
    for i in range(0, number + 1):
        print(f"{i}'s cube is {i ** 3}")

nums_cube(6)


'''
Muslim solution:
input_num = 6

for i in range(1, input_num + 1):
    print(f"Current Number is {i} and the cube is {i * i * i}")


'''