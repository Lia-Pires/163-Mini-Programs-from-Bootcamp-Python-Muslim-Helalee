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