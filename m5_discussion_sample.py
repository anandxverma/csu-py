# The operatoir module is only needed if using it instead of the basic operators
import operator as op

# Operator chaining
a = 5
b = 7
c = 9

if a < b == c:
    print(1)
else:
    print(2)

# Comparison operators
t1 = (1, 2, 3)
t2 = (0, 7, 9)

if t1 > t2:
    print(1)
else:
    print(2)

# Multi-line declarations
# Use () and "" to separate lines in a string
declaration = ("When in the Course of human events, it becomes necessary for "
               "one people to dissolve the political bands which have connected "
               "them with another, and to assume among the powers of the earth...")
print(declaration)
# multi-line example of a list
my_list = [
    1, 2, 3,
    4, 5, 6
    ]
print(my_list)

# operator module example
# using operator.contain()
# checking an integer in a list
print(op.contains([1, 2, 3, 4, 5], 2))
# checking a character in a string
print(op.contains("Hello World", "a"))

# Testing the "is" operator
s1 = "hello world"
s2 = "hello world"
print(s1 is s2)

#Example of pass
def my_func():
    pass # Do nothing

my_func()
print("The above function call did not do anything")

"""A multi-line docstring comment example
As shown here"""
