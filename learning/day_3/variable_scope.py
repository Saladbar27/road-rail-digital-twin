
import builtins

def my_min():
    pass

# Built-In scope: names that are pre-assigned in Python
# min

m = min([5, 1, 4, 2, 3])
print(m)

print(dir(builtins))

# LEGB: Local, Enclosing, Global, Built-in
# Determines the order that variables are assigned

print()

x = 'global x'

# y is a local scope (variable defined within a function)
# y doesn't live outside of the test() function

# global statement forces a variable to be global, not local
# generally don't use global much
# local is used much more frequently

def test(z):
    # global x
    x = 'local x'
    # print(y)
    print(z)

test('local z')
# print(x)

# Enclosing

def outer():
    # local to outer
    x = 'outer x'

    def inner():
        # local to inner
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)

print()