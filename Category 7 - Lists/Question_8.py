# Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
list1[2][1][2].append("h")
list1[2][1][2].append("i")
list1[2][1][2].append("j")
print(list1)


'''
Muslim solution:

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)

'''