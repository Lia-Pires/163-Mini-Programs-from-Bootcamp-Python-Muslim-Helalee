# Create a function showEmployee() in such a way that it should accept employee name, and its salary and display both. If the salary is missing in the function call assign default value 9000 for salary

def showEmployee(name, salary = 9000):
    print(f"{name}'s salary is ${salary:.2f}.")

showEmployee("Dave", 5000)
showEmployee("John")


'''
Muslim solution:

def show_employee(name, salary=9000):
    print(f"{name} has a salary of {salary}")


show_employee("John", 12000)
show_employee("Jane")


'''