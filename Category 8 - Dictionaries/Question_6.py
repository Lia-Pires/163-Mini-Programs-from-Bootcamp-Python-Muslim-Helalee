# Delete set of keys from a dictionary

from random import sample


sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
# keysToRemove = ["name", "salary"]

sampleDict.pop("name")
sampleDict.pop("salary")
print(sampleDict)

'''
Muslim solution:
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}

keysToRemove = ["name", "salary"]

sample_dict = {k: sampleDict[k] for k in sampleDict.keys() - keysToRemove}

print(sample_dict)
'''