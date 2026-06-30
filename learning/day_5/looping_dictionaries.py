
print()

my_dict = {
    'Name': 'Shelby',
    'Age': 18,
    'Height': 181,
    'Major': 'Chemical Engineering'
}

# prints keys of a dictionary
for keys in my_dict.keys():
    print(keys)

print()

# prints values of a dictionary
for fact in my_dict.values():
    print(fact)

print()

# prints keys and values of a dictionary
for key, fact in my_dict.items():
    print(key, fact)

print()

my_dict.update({"Favorite Color": "Blue"})

for key, fact in my_dict.items():
    print(key, fact)

print()

my_dict.pop("Height")

for key, fact in my_dict.items():
    print(key, fact)

print()

name = my_dict.get('Name')
print(name)

print()