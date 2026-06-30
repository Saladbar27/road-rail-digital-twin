
# Slicing: Only printing certain letters in a string
# 0:5, :5, 6:10, 6:, etc.

# Diff. of Method and Function:
# Method: Function that belongs to an object, basically the same thing for now

# .lower: Print all character of a string in lowercase
# .upper: " " uppercase
# .count(argument): counts instances of the argument in the string
# .find(argument): locates the position of the argument
#     -1 if not found

# .replace('Original', 'Replacement')
#     Must assign to a variable, same or new

# Use {} and .format to write longer strings
#     "placeholders"

# f strings: making formatting as simple as possible
#     Place variables directly into the placeholder brackets
#     Add a lowercase f at the start, outside of the quotes

# dir(variable) can show all functions for a string

# integer (int) = whole numbers
# float = numbers with decimals

distance = float(input("Enter the distance in kilometers: "))
speed = float(input("Enter the speed in kilometers per hour: "))

time = distance / speed
print(f"The time it will take to travel {distance} kilometers at {speed} kilometers per hour is {time} hours.")

