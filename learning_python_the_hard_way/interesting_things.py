# Comma separated adds a space
print "Hens", 25 + 30 / 6

# Comma separated does not add new line
print "Hello ",
print "World"

# %r shows scaped values
print "Scape sequences with 's': %s." % "\n"
print "Scape sequences with 'r': %r." % "\n"

# You can include text to show the user in parenthesis
age = raw_input("--> ")

# Unpacking wihtout [ ]
from sys import argv
script, first, second, third = argv

# Opening files
# r, w, a
file = open('file_name', 'r')


# Functions
def print_two(*args):
    arg1, arg2 = args


# Modules
import ex25_even_more_practice as ex25
from ex25_even_more_practice import print_first_and_last
ex25.break_words("this is a sentence")
print_first_and_last("hello girl!")


# Boolean
1 or True   # returns 1, python likes returning operands

# Conditionals
# if, elif, else
# elif execute in order


# Dictionaries
cities = {
    "CA": "San Francisco",
    "MI": "Detroit",
}
cities["OR"] = "Portland"
cities.get("TX", "default value")
# collections.OrderedDict


# Review getattr functionality


# INHERITANCE
class Child(Parent):
    
    def __init__(self):
        super(Child, self).__init__()
        pass

# Inheritance vs composition
"""
In composition we import a module or use another class methods instead of inherit from it
    1. Avoid multiple inheritances, it gets too complex. If you do so, get ready to navigate the class hierarchy to know 
where things are coming from
    2. Use composition to package code into modules that is used in many places
    3. Use inheritance when there are clary related reusable pieces of code that fit under a single common concept
""" 

# Magic methods
object.__dict__
object.__mro__
dir(object)

# Comments
"""
When you write comments, describe why you are doing what you are doing. The code already says how, but why you did
things the way you did is more important.
"""