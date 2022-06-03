# Print the following pattern

"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""

for N in range(1, 6, 1):
    print("*" * N)
for N in range(6, 0, -1):
    print("*" * N)

'''
Muslim solution: 
rows = 5

for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=" ")
    print("\n")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=" ")
    print("\n")
    
'''
