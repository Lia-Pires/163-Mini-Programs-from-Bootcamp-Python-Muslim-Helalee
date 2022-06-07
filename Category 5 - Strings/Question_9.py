# Removal all the characters other than integers from a string

def just_integers(string):
    new_string = "".join([item for item in string if item.isdigit()])
    print(f"The new string is: {new_string}")


just_integers('I am 25 years and 10 months old')


'''
Muslim solution:

str = 'I am 25 years and 10 months old'

result = "".join([item for item in str if item.isdigit()])

print(result)

'''
