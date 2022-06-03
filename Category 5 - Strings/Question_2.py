# Count all lower case, upper case, digits, and special symbols from a given string

str = "h@#el26a^&5le"



def counter(str):
    lower = 0
    upper = 0
    digit = 0
    special = 0
    for char in str:
        if char.islower():
            lower += 1
        elif char.isupper():
            upper += 1
        elif char.isdigit():
            digit += 1
        else:
            special += 1
    
    print(f"In the given string ({str}) there are {lower} lower characteres, {upper} upper characteres, {digit} digits and {special} special characteres ")

counter("h@#el26aB^&5le")
counter("H1351fkgnsAFJOE&*#")
