# Reverse a given number and return true if it is the same as the original number

num1 = 323

num2 = 625




'''Muslim Solution:
def reverse_check(number):
    print("Original Number:", number)

    original_num = number
    reversed_num = 0

    while (number > 0):
        remainder = number % 10

        reversed_num = (reversed_num * 10) + remainder

        number = number // 10

    if original_num == reversed_num:
        return True

    else:
        return False


print("Original is the same as the Reversed:", reverse_check(787))
'''