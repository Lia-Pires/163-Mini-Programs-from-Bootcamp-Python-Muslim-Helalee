# Given an input string, count occurrences of all characters within a string

def count_chars(string):
    chars = {}
    for i in string.lower():
        string = string.lower()
        chars.update({i:string.count(i)})
    print(chars)
        

count_chars("testing, 1, 2, 3 testing")
count_chars("Python is Awesome")



'''Muslim solution:

str = "Lemon Malt"
str = "kiwi"

count_dict = dict()

for char in str:
    count = str.count(char)

    count_dict[char] = count

print(count_dict)

'''

