# Remove empty strings from a list of strings

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

def remove_empty(list):
    for i in list:
        if i == None or i == "":
            list.remove(i)
    print(list)

remove_empty(["Emma", "Jon", "", "Kelly", None, "Eric", ""])


'''
Muslim solution:

str_list = ["Emma", "John", "", "Kelly", None, "Eric", ""]

new_str_list = list(filter(None, str_list))
print(new_str_list)


'''
