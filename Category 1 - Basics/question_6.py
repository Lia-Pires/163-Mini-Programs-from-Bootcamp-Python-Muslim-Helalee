# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

def iterate_div_5(list):
    print("Numbers on which are divisible of 5: ")
    for number in list:
        if number % 5 == 0:
            print(number)
        

iterate_div_5([10, 20, 33, 46, 55, 77, 105, 204, 335])



'''Muslim solution:
def divisible_by_5(num_list):
    print("Given List", num_list)

    for num in num_list:
        if (num % 5 == 0):
            print("Divisible by 5:", num)


list = [10, 20, 33, 46, 55, 77, 105, 204, 335]
divisible_by_5(list)
'''