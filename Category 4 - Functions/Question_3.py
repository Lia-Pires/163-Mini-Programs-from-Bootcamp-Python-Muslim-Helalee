# Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of them. And also it must return both addition and subtraction in a single return call

def calculation(num_1, num_2): 
    addition = num_1 + num_2
    subtraction = num_1 - num_2
    return addition, subtraction

result = calculation(5, 6)
print(result)



'''
Muslim solution:

def calculation(a, b):
    return a + b, a - b


result = calculation(40, 10)
print(result)

'''