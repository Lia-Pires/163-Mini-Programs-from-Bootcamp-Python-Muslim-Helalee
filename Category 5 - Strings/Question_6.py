# Find the last position of a substring “Kelly” in a given string


def count_kelly(string):
    print(string.count("Kelly"))



count_kelly("Kelly is a data scientist who knows Python. Kelly works at google."
)    


'''Muslim solution:
str = "Kelly is a data scientist who knows Python. Kelly works at google."

index = str.rfind("Kelly")
print(index)

'''