
# https://pythonmasterhome.files.wordpress.com/2019/07/hw0507.pdf

'''
1. slice returns a range of characters.
2. Concatenatation merges strings, in Python using the operator +.
3. List comprehension allows more concise syntax when creating a list based on an existing list.
4. Dictionaries are a data type used to store information in pairs of key (unique) and value.
5. The key in the dictionary can be of any immutable type (numbers and strings), values of any type.
6. Entry is an item in a dictionary. In Python, a dictionary item is in format key:value.
7. Dictionaries as saved as JSONs.
8. Dictionaries are defined with squiggly brackets:
*create
dict5 = {
  "a": "aaaaa",
  "b": "bbbbbbtang"
}
*add - using a key and adding a value to it
dict5["c"] = "cccccc"
*update (will add if doesn't exist)
dict5.update({"c": "ccccccccccccccc"})
*remove
by key: dict5.pop("a")
OR
del dict5["a]

9. The method keys() returns a list of the keys existing in the dictionary.
10. The method items() returns a list of tuples containing key-value items in the dictionary.

'''

# ex11
str11 = 'I love to eat ice cream in the beach'               # this should probably be "at" the beach

upper11 = str11.upper().split()
print(upper11)
firstletters = [x[:1] for x in str11.split()]
print(firstletters)
thirdletters = [x[2:] for x in str11.split() if len(x) >= 3]
print(thirdletters)
lengthwords = [len(x) for x in str11.split()]
print(lengthwords)

# ex12
facts = [10 ** x for x in range(1, 10)]
print(facts)

# ex13
def tryGetValue(dictionary, key):
    if key in dictionary:
        return dictionary.get(key)
    else:
        return None

# ex14
def getSortedKeys(dictionary):
    list_keys = []
    for key in dictionary:
        list_keys.append(key)
    list_keys.sort()
    return list_keys

# ex15
def mergeDictionary(dict1, dict2):
    temp_dict = dict1.copy()
    temp_dict.update(dict2)
    return temp_dict

# ex16
person_list = {}
while True:
    id = int(input('Please enter ID number (-1 to exit): '))
    if id == -1:
        break
    if id in person_list:
        print('ID already exists in the list!')
        continue
    name = input('Please enter full name: ')
    person_list[id] = name

if person_list != {}:
    print('THE LIST:', person_list)
else:
    print("List is empty!")

