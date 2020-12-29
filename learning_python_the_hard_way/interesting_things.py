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