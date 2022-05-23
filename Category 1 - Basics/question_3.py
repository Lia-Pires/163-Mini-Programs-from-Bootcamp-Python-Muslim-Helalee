# In a string, display the characters at the even indices

def even_indices(string):
    print("Characters in even indices: ", string[0:-1:2])


even_indices("Hi, i'm Goku")





'''Muslim solution:
def print_even_index(str):

    for char in range(0, len(str), 2):
        print("Index[", char, "]", str[char])


string = "learning"
print_even_index(string)
'''