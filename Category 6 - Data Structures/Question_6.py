# Given two sets, Checks if One Set is a subset or superset of another Set. if the subset is found delete all elements from that set

from turtle import clear

def subset(set_1, set_2):
    print(f"Is the fisrt set subset of the second set? {set_1.issubset(set_2)}")
    print(f"Is the fisrt set superset of the second set? {set_1.issuperset(set_2)}")
    print(f"Is the second set subset of the first set? {set_2.issubset(set_1)}")
    print(f"Is the second set superset of the first set? {set_2.issuperset(set_1)}")
    if set_1.issubset(set_2):
        set_1.clear()
        print(f"The remaining set is: {set_2}")

    if set_2.issubset(set_1):
        set_2.clear()
        print(f"The remaining set is: {set_1}")


   
subset({27, 43, 34}, {34, 93, 22, 27, 43, 53, 48})


'''
Muslim solution:

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

print("First set is a subset of the second set", first_set.issubset(second_set))
print("Second set is a subset of the first set", second_set.issubset(first_set))


print("First set is a super set of the second set",
      first_set.issuperset(second_set))
print("Second set is a super set of the first set",
      second_set.issuperset(first_set))


if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()


print(first_set)
print(second_set)


'''

