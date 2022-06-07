# Arrange string characters such that lowercase letters should come first

lower_chars = []
upper_chars = []


def upper_lower(str):
    for letter in str:
        if letter.islower():
            lower_chars.append(letter)
        else:
            upper_chars.append(letter)
    final_string = "".join(lower_chars + upper_chars)
    print(final_string) 


upper_lower("PyThon")



'''Muslim Solution:
str = "Json"
lower = []
upper = []

for char in str:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

sorted_string = "".join(lower + upper)
print(sorted_string)

'''