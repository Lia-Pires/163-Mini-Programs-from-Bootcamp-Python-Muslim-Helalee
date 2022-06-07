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


'''Muslim solution:

def find_digits_chars_symbols(str):
    char_count = 0
    digit_count = 0
    symbol_count = 0

    for char in str:
        if char.islower() or char.isupper():
            char_count += 1
        elif char.isnumeric():
            digit_count += 1
        else:
            symbol_count += 1

    print(
        f"Character Count: {char_count}, Digit Count: {digit_count}, Symbol Count: {symbol_count}")


str = "h@#el26a^&5le"

find_digits_chars_symbols(str)

'''