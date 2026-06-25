
# To create a list, use square brackets []
# len(variable) to see how many items in a list
# "index" for a list starts at 0, access a specific item using square brackets in the print

# using print(variable[-1]) gives the last item in the list. Good trick.
# print(variable[0:2]) gives 0 and 1 index, but NOT 2

# .append(item) adds an item to the end of a list
# .insert(index, item) adds an item to a specific index in a list
# .extend(list) adds a list to the end of another list
# .remove(item) removes an item from a list
# .pop() removes the last item in a list, can be saved as a variable and printed to see what was removed

# .reverse() reverses the order of a list
# .sort() sorts a list in alphabetical order, or numerical order if numbers are in the list
# reverse argument can be added to both .sort() and .reverse() to reverse the order of the list
# sorted(list) returns a sorted list, but does not change the original list

# min(list) returns the smallest item in a list
# max(list) returns the largest item in a list

# .index(item) returns the index of an item in a list
# ('item' in list) returns True or False if the item is in the list
# enumerate(list) returns the index and item in a list, can be used in a for loop to print both index and item

# .join(list) joins a list into a string
# .split(string) splits a string into a list

# A tuple cannot be modified
# Lists are mutable, tuples are immutable
# Lists use square brackets []
# Tuples use parentheses ()

# Sets are values that are unordered and have no duplicates
# Uses could be to test if a value is a part of a set or to remove duplicate values
# .intersection(set) returns the common values between two sets
# .difference(set) returns the values that are in one set but not the other
# .union(set) returns all the values from both sets, but no duplicates

# Empty Lists
empty_list = []

# Empty Tuples
empty_tuple = ()

# Empty Sets
empty_set = {} # This isn't right! It creates an empty Dictionary.
empty_set = set()