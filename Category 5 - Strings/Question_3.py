# Find all occurrences of “is” in a given string ignoring the case


def find_in_string(string, str):
    new_string = string.lower()
    print(string.count(str.lower()))
    

find_in_string("My cat is awesome. Your cat is amazing. Is his cat asleep?", "Is")



'''Muslim solution:

str = "My cat is awesome. You're cat is amazing. Is her cat asleep?"

sub_string = "is"

temp_string = str.lower()

count = temp_string.count(sub_string.lower())

print(count)

'''