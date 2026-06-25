
# def keyword to define a function
# use pass operation to leave a function empty without causing an error
# use parenthesis after calling a function to execute it

# benefit of functions is the ability to store hundreds of operations in one place
# changing ! to . example, instead of changing it manually 100 times you can just change the function.
# "Keeping your code DRY"

# A FUNCTION IS A MACHINE THAT TAKES INPUT AND PRODUCES AN OUTPUT

# For adding arguments to a function, they must be defined. See below. They must be in order.

print ()

def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)

print(hello_func('Hi', name = 'Shelby'))


# *args and **kwargs allow us to accept an arbitrary number of positional or key word arguments
# *list and **dictionary unpacks the list and dictionary respectively

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)


# example that ties everything from all videos together so far
"""Triple Quotes is a Doc String, essentially allows for keeping track of what a function does"""

# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]

print(is_leap(2020))
print(days_in_month(2017, 2))

print()