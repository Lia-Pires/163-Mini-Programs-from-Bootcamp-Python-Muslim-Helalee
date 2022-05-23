#  Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string

def strip_string(string, n):
    print(f"String from indice {n+1} to the end:", string[n:-1:1])



strip_string("I know that I know nothing", 8)



'''Muslim solution:
def remove_chars(str, num):
    return str[num:]


print(remove_chars("learning", 4))
'''