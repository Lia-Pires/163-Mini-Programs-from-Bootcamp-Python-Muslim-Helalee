#  Print multiplication table from 1 to 10

def multiplication_table(number):
    for n in range(10):
        print(f"{n + 1} x {number} = {(n + 1) * number} ")



multiplication_table(1)
multiplication_table(2)
multiplication_table(3)
multiplication_table(4)
multiplication_table(5)
multiplication_table(6)
multiplication_table(7)
multiplication_table(8)
multiplication_table(9)
multiplication_table(10)


'''
Muslim solution:
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print("\t\t")
    
'''