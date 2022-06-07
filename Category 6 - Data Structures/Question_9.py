# Remove duplicate from a list and create a tuple and find the minimum and maximum number

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
temp_set = set(sample_list)
final_tuple = tuple(temp_set)

print(f"The final tuple is: {final_tuple} and it's minimum and maximum number are: {min(final_tuple), max(final_tuple)}")


'''
Muslim solution:
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

list = list(set(sample_list))
print(list)

tuple = tuple(list)
print(tuple)

print("Min:", min(tuple))
print("Max:", max(tuple))

'''
