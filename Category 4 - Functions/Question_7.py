# Assign a different name to a function and call it with the new name

def area(a, b):
    return a * b

square_meters = area
result = square_meters(5, 4)
print(result)

'''
Muslim solution

def display_student(name, age):
    print(name, age)


display_student("Emma", 34)

show_student = display_student

show_student("Jelly", 24)

'''