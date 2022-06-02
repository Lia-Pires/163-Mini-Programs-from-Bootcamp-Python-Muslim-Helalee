# Write a function called exponent(base, exp) that returns an int value of base raised to the power of exp.

def power_function(base,xp):
    result = base
    for n in range(xp-1):
        result = result * base
    print(f"The number {base} raised to the power of {xp} is {result}")

power_function(2, 2)
power_function(4, 2)
power_function(3, 2)
power_function(3, 3)
power_function(8, 3)
power_function(8, 7)



'''
Muslim Solution:
def exponent(base, exp):
    num = exp
    result = 1

    while num > 0:
        result = result * base
        num = num - 1

    print(base, "raised to the power of", exp, "is", result)


exponent(5, 3)
'''