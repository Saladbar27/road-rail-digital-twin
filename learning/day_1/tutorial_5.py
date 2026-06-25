
# Dictionaries, can be updated
# variable = {'key': 'value', 'key2': 'value2'}

# .get() method returns None if the key does not exist, or you can specify a default value to return if the key 
# does not exist
# .update() method can be used to update a dictionary with new key-value pairs, or to change the value of an existing key
# .del keyword can be used to delete a key-value pair from a dictionary
# .pop can remove and also return a key-value pair from a dictionary

# .keys() method returns a list of all the keys in a dictionary
# .values() method returns a list of all the values in a dictionary
# .items() method returns a list of all the key-value pairs in a dictionary as tuples


student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

for key, value in student.items():
    print(key, value)