# Print the result of the multiplication of two sets of integers if it is less than 1000. If the result is greater that 1000, print their sum.

def result_func(x, y):
    product = x * y

    if product < 1000:
        print(f"product < 1000: {product}")
    else:
        print(f"product > 1000, numbers sum: {x+y}")


result = result_func(200, 20)
result = result_func(5, 10)




'''Muslim solution:
def multiplication_or_addition(num1, num2):
    product = num1 * num2

    if product <= 1000:
        return product

    else:
        return num1 + num2


result = multiplication_or_addition(35, 36)
print(result)'''


