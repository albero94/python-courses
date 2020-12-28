from sys import argv

i = 0
numbers = []
if len(argv) == 2:
    _, limit = argv
else:
    print "Please input the number limit."
    exit()

while i < int(limit):
    print "At the top i is {}" .format(i)
    numbers.append(i)
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is {}" .format(i)

print "The numbers: {}" .format(numbers)