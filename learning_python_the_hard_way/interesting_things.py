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