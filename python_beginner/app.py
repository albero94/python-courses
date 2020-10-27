print("Hello World!")

# VARIABLES
age = 20
first_name = "Laura"
last_name = "Ferrando"
price = 19.95
is_online = False
print(age)
print(f"{first_name} {last_name} is {age} years old.")

# 1_000  use _ for thousand separators



# RECEIVE INPUT
name = input("What is your name? ")
print(f"Hello {name}")



# TYPE CONVERSION
# numbers (int, float, complex), strings and booleans
birth_year = input("Enter your birth year: ")
age = 2020 - int(birth_year)
print(f"You are {age} years old")

# conversion functions
# int() float() bool() str()
first = input("Enter first number: ")
second = input("Enter second number: ")
print(float(first) + float(second))



# STRINGS
# strings are immutable
course = "Python for Beginners"
print(course.upper())
print(course.find("y"))
print("Python" in course)
print(course.replace("for", "4"))



# ARITHMETIC OPERATORS
# + - * / % //(integer division) **(exponent)
# += ...


# COMPARISON OPERATORS
# > < >= <= == != 


# LOGICAL OPERATORS
# and or not
print (5<10 and 5>1) 



# IF STATEMENTS
temperature = 25
if temperature > 30:
    print("It's a hot day")
elif temperature > 20:
    print("It's a nice day")
else:
    print("It's a cold day")
print("Done")



# EXERCISE: WEIGHT CONVERSION
weight = float(input("Weight: "))
unit = input("(K)s or (L)bs: ")

if unit.lower() == "k":
    print("Weight in Lbs: " + str(weight * 2.2))
elif unit.lower() == "l":
    print("Weight in Kg: " + str(weight/2.2))
else:
    print("Units not valid (K, k) (L, l)")



# WHILE LOOPS
number = 0
while number<5:
    print(number * "*")
    number += 1


# LISTS
# can use negative indexes (I like this :) )
names = ["Alvaro", "Smith", "Mary", "Jose", "Joe"]
print(names)
print(names[-1])    
names[1] = "John"
print(names[1:3])



# LIST METHODS
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

numbers.insert(2, 10)
print(numbers)
print(10 in numbers)
numbers.remove(10)
print(10 in numbers)
print(len(numbers))
numbers.clear()         # empties list



# 2D LISTS
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_grid[1][2])
for row in number_grid:
    for number in row:
        print (number)



# FOR LOOPS
names = ["Alvaro", "Smith", "Mary", "Jose", "Joe"]
for name in names:
    print(name)



# RANGE FUNCTION
for number in range(5, 10, 2):
    print(number)



# TUPLES
# like lists but immutable
numbers = (1, 2, 3, 3)
# numbers[0] = 5, you get an error
# no append and other functions like those
numbers.count(3)    # 2


# reference to magic methods __add__ and others


# FUNCTIONS
def say_hi(user_name: str, age: int):
    print(f"Hello {user_name} you are {age} years old")

say_hi("Alvaro", 26)

def sum_integers(int1: int, int2: int) -> str:
    return str(int1 + int2)
sum_integers(5, 10)



# DICTIONARIES
# allows to store information in key value pairs (hash), no duplicates
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    4: "April",
    5: "May"
}
print(month_conversions)
print(month_conversions["Jan"])                     # throws exception if key not found
print(month_conversions[4])                         
print(month_conversions.get("Dec", "Default"))      # falls back to default if key not found



# TRY EXCEPT
try:
    num = int(input("Enter a number: "))        # this only works if they enter an integer
    print(num)
    value = 10/0
except ValueError as err:
    print("Invalid input")
    print(err)
except ZeroDivisionError as err:
    print("Divided by 0")
    print(err)



# READING FILES
employee_file = open("employees.txt", "r")        # r, w, r+ (read and write), a (append)

employee_file.readable()        # boolean
employee_file.read()            # reads whole file
employee_file.readline()        # reads one line and moves cursor
employee_file.readlines()       # reads each line and returns an array with their content

for line in employee_file.readlines():
    print(line)

employee_file.close()



# WRITING TO FILES
employee_file = open("employees.txt", "a")
employee_file.write("\nAlvaro - Software Engineer")

employee_file = open("employees1.txt", "w")
employee_file.write("Alvaro - Software Engineer")



# MODULES AND PIP
# import a python file and be able to access all that information
# list of python modules available in python documentation
# built in modules, already in the language
# external modules, can be installed through pip

import useful_tools
from useful_tools import get_file_ext, roll_dice
print(useful_tools.beatles)
print(get_file_ext("example.jpg"))
print(roll_dice(6))

# pip install python-docx
# import docx
# docx.something



# CLASSES AND OBJECTS
from Student import Student

student1 = Student("Alvaro", "CS", 4.0, False)
print(student1.name) 
print(student1.print_info())



# INHERITANCE
from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_chicken()
myChef.make_salad()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_fried_rice()
myChineseChef.make_special_dish()