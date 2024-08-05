# INTRODUCTION TO WORKING IN PYTHON
# Based on "Learn the Basics" tutorial in learnpython.org: https://www.learnpython.org/#google_vignette


############################################
########## BEFORE RUNNING SCRIPT! ##########
############################################

# Make sure desired libraries are downloaded in you desired
# mamba environment OUTSIDE OF PYTHON IN TERMINAL
# cd
# mamba create -n python_learning_2024
# mamba activate python_learning_2024
# mamba install python pandas numpy

# Using python_learning_2024 mamba virtual environment


##################################
##################################
##################################



# GENERAL SYNTAX + OBJECT ENV


# Print a string
print("This line will be printed")

# For code indentation, best to use 4 spaces
x = 1
if x == 1:
    # indented 4 spaces
    print("x is 1.")

# To view all objects, go to Jupyter interactive window, click on ellipses (...),
# then select "Variables"
    
# Python uses 0 to indicate the 1st element/index of an object
mylist = [1, 2, 3]
print(mylist[0])

# Delete individual objects
del x



##################################
##################################
##################################


# VARIABLES    


# Python supports integers (whole numbers), floating point numbers (decimals), and complex numbers
myint = 7
print(myint)

# Can define a float using several different notations
# Notation 1
myfloat = 7.0
print(myfloat)
# Notation 2
myfloat1 = float(7)
print(myfloat1)

# Strings are defined with either a single or double quote
# Double quotes makes it easier to include apostrophes in a string
mystring1 = 'hello'
print(mystring1)
mystring2 = "Don't worry about apostrophes"
print(mystring2)

# One can use operators to combine multiple defined objects
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
hellowworld = hello + " " + world
print(hellowworld)

# >1 variable assignments to >1 object can be done on the same line
a, b = 3, 4
print(a, b)

# You CANNOT use operators to combine number and string objects
print(one + two + hello)

####################
##### EXERCISE #####
####################

mystring = "hello"
myfloat = 10.0
myint = 20

if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)


##################################
##################################
##################################


# LISTS
# Can contain any type of variable & as many variables as desired
# Can be iterated over and added to in a sample manner using .append() after the list name


# Lists are defined using square brackets []
mylist = []

# Add to existing list using .append()
mylist.append(1)
mylist.append(2)
mylist.append(3)

# Each list element will be separated by a comma within the list
print(mylist)

# Print elements within list
print(mylist[0]) # print the 1st element in mylist
print(mylist[1]) # print the 1st element in mylist
print(mylist[2]) # print the 1st element in mylist

# Prints out 1,2,3 each in its own line
for x in mylist:
    print(x)

####################
##### EXERCISE #####
####################

number = [1, 2, 3]
strings = ["hello", "world"]
names = ["John", "Eric", "Jessica"]

second_name = names[1]

print(number)
print(strings)
print("The second name of the list is %s" % second_name)


##################################
##################################
##################################


# ARITHMETIC OPERATORS


# Python follows order of operations like expected
number = 1 + 2 * 3 / 4.0
print(number)

# Print the 1st digit remainder of 3 / 11
3 / 11
remainder1 = 11 % 3
print(remainder1)

# Two multiplication symbols in a row = power relationship
squared = 7 ** 2
cubed = 2 ** 3
print (squared, cubed)

# Can use operators to duplicate the number of a variable
lotsofhellos = "hello " * 10
print(lotsofhellos)

# Can combine lists into one list using + operator
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# Can form a new list with a repeating sequence using * operator
print([1,2,3] * 3)

####################
##### EXERCISE #####
####################

x = object() # empty object
y = object()

x_list = [x] * 10 # put 10 empty objects from x into x_list: does NOT print 10 x's
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")


##################################
##################################
##################################


# STRING FORMATTING


# Use an argument specifier (% operator) to insert an object inside a format string
# Format string = normal text with arguent specifier
# Exs of argument specifiers: %, %s (string), %d (integer)
name = "John"
print("Hello, %s!" % name)

# To use ≥ 2 argument specifiers, use a tuple (aka parenthesis)
age = 23
print("%s is %d years old." % (name, age))

# Can convert a non-string object into a string using the % operator
mylist = [1, 2, 3]
print("A list: %s" % mylist)

####################
##### EXERCISE #####
####################

# %.2f = print 2 digits after decimal for float number 
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is %.2f"

print(format_string % data)


##################################
##################################
##################################


# BASIC STRING OPERATIONS


# To print quotes in a string, need to surround with double quotes
print("single quotes are ' '")

# Length of a string is calc by # of characters, punctuation marks, AND spaces
astring = "Hello world!"
print(len(astring)) # output = 12

# Counts the position of the 1st o in "Hello World!"
# REMEMBER: Python starts counting elememts (indices) at 0
print(astring.index("o"))

# Count the # of occurrences of "l"
print(astring.count("l"))

# Print all characters between indices 3 to 6
# 3:7 = tells Python: "give me characters between 3 and UP TO 7 (NOT including 7)"
print(astring[3:7])

# Starting with 3, Print every 2nd character between indices 3 to 6
# splice syntax = [start:stop:step]
print(astring[3:7:2]) # output = D "" (aka space)

# Starting with 3, print every 1st character between indices 3 to 6
print(astring[3:7:1])

# Can use splice syntax to reverse a string
# start = all characters (:)
# stop = all characters (:)
# step = -1 (print each character starting from the end of the string)
print(astring[::-1])

# Convert all string characters to upper and lowercase 
print(astring.upper())
print(astring.lower())

# Does the object's string start/end with a user-defined string?
# .startswith() and .endswith () are Boolean functions (i.e. True or False)
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

# Split a string into a list based on a user-defined character/delimiter
astring.split(" ")

####################
##### EXERCISE #####
####################

# Create a string that fulfills all of the print statements
s = "Strings are awesome!"

# Length should be 20
print("Length of s = %d" % len(s))
# Should be index 8
print("The first occurrence of the letter a = %d" % s.index("a"))
# Number of a's should be 2
print("a occurs %d times" % s.count("a"))
# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")
# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")
# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))


##################################
##################################
##################################


# CONDITIONS


# Evaluate whether x contains certain values
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

# Double == --> equal to
name = "John"
age = 23

if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# "in" specifies whether a variable exists within an object/list
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

# If/ifelse statements need code blocks (aka spaces or tabs)
# Python uses 4 spaces, but you can use whatever, AS LONG AS
# block length consistent across lines
statement = False
another_statement = True

if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

# Ifelse statement example
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

# "is" operator compares the variable itself, whereas == compares
# elements WITHIN the variable
x = [1,2,3]
y = [1,2,3]

print(x == y) # True: both x and y have [1,2,3]
print(x is y) # False: the object x itself is not y

# "not" inverts a Boolean expression
print(not False) # True
print((not False) == (False)) # False, b/c not False = True, and True doesn't equal False

####################
##### EXERCISE #####
####################

# Make sure varibles w/in objects resolve each statement as True

number = 16
second_number = 0
first_array = [1, 2, 3]
second_array = [4, 5]

if number > 15:
    print("1")

# If first_array contains any variables
if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

# If first_array contains any variables AND 1st index is 1
if first_array and first_array[0] == 1:
    print("5")

# If second_number does NOT contain any variables
# Empty variables = "", [], 0, False
if not second_number:  
    print("6")


##################################
##################################
##################################


# LOOPS


####################
#### FOR LOOPS #####
####################

# "FOR" loops iterate over a given sequence, then stop after iterating
# through all variables
primes = [2, 3, 5, 7]
for prime in primes: # for each element within the primes object
    print(prime)

# For loops can iterate over a sequence of numbers using range() and xrange()
# range() in Python 3+ = returns an iterator of range values
# Print out range of numbers 0 - 5
for x in range(5):
    print(x)

# Print values from 3 UP TO 6 (NOT including 6)
for x in range(3, 6):
    print(x)

# For numbers between 3 and 8, starting with 3, 
# print every 2nd number (variable)
for x in range(3, 8, 2):
    print(x)

####################
#### WHILE LOOPS ###
####################
    
# "WHILE" loops repeat as long as a Boolean argument is met
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

####################
# BREAK & CONTINUE #
####################

# Break = exit the for/while loop
count = 0
while True:
    print(count) # print the number that's being iterated IF the "if count >= 5" statement is True
    count += 1 # count = count + 1
    if count >= 5: # return to while statement until count >= 5
        break

# Continue = once a variable satisfies the for/while condition is met,
# return to original for/while loop
# Here, if x is even, return back to the "for x in range(10)" statement
    # If x is NOT even, print x
for x in range(10):
    if x % 2 == 0: # check if x is even
        continue
    print(x)

####################
### ELSE CLAUSE ###
####################

# When the for/while loop condition fails, then the code written under
# the "else" clause is executed
count = 0
while(count < 5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# If a break statement is executed BEFORE the else clause,
# else is skipped
for i in range(1, 10):
    if(i % 5 == 0): # if remainder of number / 5 is 0...
        break # exit the loop, or...
    print(i) # print that number
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

####################
##### EXERCISE #####
####################

# Print all even numbers from the list in list order,
# and stop once reach 237
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number == 237:
        break
    else:
        if number % 2 == 0: # if remainder of number / 2 is 0
            print(number)



##################################
##################################
##################################


# FUNCTIONS
# Are a convenient way to divide code into useful blocks
# that make code reusable and time saving


# Functions are defined using "def" followed by user-defined function name
def my_function():
    print("Hello From My Function!")
my_function()

# Can also receive arguments
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s!"%(username, greeting))
my_function_with_args("Taylor", "a Happy Holiday")

# Can return a value to the user using "return" 
def sum_two_numbers(a, b):
    return a + b
sum_two_numbers(4, 6)

####################
##### EXERCISE #####
####################

# Return list of strings
def list_benefits():
    return ["More organized code",
            "More readable code",
            "Easier code reuse",
            "Allowing programmers to share and connect code together"]

# Concate user-defined string and " is a benefit of functions!" statement
def build_sentence(info):
    return info + " is a benefit of functions!"

# Create a code that combines data from list_benefits()
# and build_sentence()
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits() # store list of strings as list_of_benefits object
    for benefit in list_of_benefits: # for each variable in list_of_benefits
        print(build_sentence(benefit)) # add variable from list_of_benefits within build_sentence() & print

name_the_benefits_of_functions()


##################################
##################################
##################################


# CLASSES & OBJECTS
# Classes: template to create an object
# Objects: encapsulation of variables and functions into a single entity

# Create a class called "MyClass", which contains a variable & function
# The point of this is to apply a set of parameters to multiple conditions
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjectx

# Assess the variable stored in myobjectx
myobjectx.variable

# You can create multiple objects of the same class 
# (i.e. multiple objects that use the same variables and/or functions)
# Here, myobjectx and myobjecty both have a "variable" object,
# and you can assign/replace new variables to the "variable" object
myobjecty = MyClass()
myobjecty.variable = "yackity"

print(myobjectx.variable)
print(myobjecty.variable)

# To use function() from MyClass, call .function() after the object's name 
myobjectx.function()
myobjecty.function()

# __init__(): function used for assigning values in a class
# (i.e. when a class is being initiated)
class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber())

# My Example: calculate the sum of a list of list of numbers
# Here, whole point = execute the same desired function(s) for different
# input variables
# Create a class where you input a list of numbers 
# and get a statement showing the sum
class SumCalculator:
    def __init__(self, list_numbers):
       self.list_numbers = list_numbers
       
    def returnSum(self):
        nums_str_format = " + ".join(str(num) for num in self.list_numbers)
        sum_list = sum(self.list_numbers)
        return "%s = %s." % (nums_str_format, sum_list)

# Provide user-definied list of list of numbers
nums_list = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12]]

# Run 
for group_nums in nums_list:
    nums = SumCalculator(group_nums)
    print(nums.returnSum())

####################
##### EXERCISE #####
####################

# Create a Vehicle class and create 2 vehicles with following parameters:
# car 1 = red convertible, $60,000.00, named Fer
# car 2 = blue van, $10,000.00, named Jump

# Define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Create car1 and car2 objects
car1 = Vehicle()
car1.name = "Fehr"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000

# test code
print(car1.description())
print(car2.description())

# My example
# Count the # of AAs for a given protein
class NeoantigenLengthCalc:
    def __init__(self, kmer_seq):
       self.kmer_seq = kmer_seq

    def kmer_description(self):
        kmer_length = len(self.kmer_seq)
        return "Neoantigen sequence %s is %s amino acids long." % (self.kmer_seq, kmer_length)
 
kmer_seqs = ['MVLASDDASKFHASDASDFIH',
             'ASOEIYSLKF',
             'PEIOHRFQIWNFSAUIEFSOIHNFOQWFISUPHDF']

# Run 
for kmer in (kmer_seqs):
    kmer_data = NeoantigenLengthCalc(kmer)
    print(kmer_data.kmer_description())


##################################
##################################
##################################


# DICTIONARIES
# Works with keys and values
# Keys = unique identifiers for values; can be any type of object
# Values = data that can be accessed using keys


# Example 1: database of phone numbers can be stored using a dictionary
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

# Example 2
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

# One can iterate over dictioinaries, 
# but dictionaries don't keep order of values stored in it
# To iterate over key-value pairs (aka show the values for each key),
# # use .items() after the dictionary name
# Name = key, number = value
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# To remove a key-value pair from a dictionary, use del or .pop
del phonebook["John"]
print(phonebook)

# OR
phonebook.pop("John")
print(phonebook)


####################
##### EXERCISE #####
####################


# Add "Jake" to phonebook with phone number 938273443
# Remove Jill from phonebook

# Original phonebook
phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
} 

# Add Jake with his number
phonebook["Jake"] = 938273443

# Remove Jill
phonebook.pop("Jill")

# Test code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")


##################################
##################################
##################################


# MODULES AND PACKAGES
# Module = piece of software with a specific functionality
    # In python, modules = Python files with a .py extension
    # Each module is made up of a different file, which may be edited separately
    # Modules can have set of fxns, classes, variables that are defined and implemented
# Package = set of python modules
# Library = collection of packages


# Example module called "mygame"
    # directory = mygame/
    # modules "game" and draw"
        # mygame/game.py
        # mygame/draw.py

# Script from draw.py module:
def draw_game():
    ...

def clear_screen(screen):
    ...

# Script for the game.py module:
# Import the draw module (from draw.py) as a package
import draw

def play_game():
    ...

def main():
    result = play_game() # play_game() is from "game" module, so don't need to specify game.play_game()
    draw.draw_game(result) # draw_game() from "draw" module, which has been imported as a package

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()

# NOTE: when python imports a module, creates a .pyc file
# .pyc = python compiled file = file compiled into bytecode so won't have to
# parse the original .py file each time want to load the module

# Namespace = system where each object named and can be accessed in Python
# Example: import draw_game() into namespace using "from" command
# so that you don't have to call draw.draw_game() whenever you want to use draw_game()
from draw import draw_game

def main():
    result = play_game()
    draw_game(result)

# If want to import all objects from a module, use *
from draw import *

# The 1st time a module is loaded into Python, it's initialized by
# executing the module's code once
# If another module in your code imports a previously loaded module,
# it won't be loaded again = any local variables from said module = "singleton"
# Singleton = variables initialized only once

# Example: in draw.py module, initialize main_screen object as a singleton
class Screen():
    ...

def clear_screen(screen):
    ...

def draw_game():
    # when clearing the screen we can use the main screen object initialized in this module
    clear_screen(main_screen)

# initialize main_screen as a singleton
main_screen = Screen()

# Can tell python interpreter where to look for modules
# using PYTHONPATH environment variable in terminal
# Aside from default local directory & built in modules,
# PYTHONPATH gives additional directories to search for modules
# PYTHONPATH=/path/directory python game.py

# Can also use sys.path.append()
# NOTE: execute this BEFORE running import command
import sys
sys.path.append("/path/directory")

# Exploring modules: dir() and help()
# Import module "urllib" and look for its functions
import urllib
dir(urllib)

# Read more about the request()
help(urllib.request)

# Packages = namespaces containing multiple modules (& packages)
# Aka directories with certain requirements
# MUST contain __init__.py file: indicates that the directory __init__.py is in
# is a Python package --> allows package to be imported as a module

# Example: we create a "foo" directory --> foo = package name
#  In foo, create modules __init__.py and bar.py
# Can import "bar" module in 2 ways:
import foo.bar # in rest of code, will have to use foo.bar.function() each time
from foo import bar # in rest of code, won't need to use foo prefix; need to use bar.function()


####################
##### EXERCISE #####
####################


# Print alphabetically sorted list of all functions in 
# "re" module containing the word "find"
import re
re_fxns = dir(re)
find_members = [fxn for fxn in re_fxns if 'find' in fxn]
find_members = sorted(find_members)


##################################
##################################
##################################


# NUMPY ARRAYS
# Numpy arrays fast, easy to work with,
# can perform calculations across entire arrays

# From 2 python lists, create numpy arrays
import numpy as np

height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_height = np.array(height)
np_weight = np.array(weight)

print(np_height)
print(np_weight)

# Print type to make sure numpy array
print(type(np_height))
print(type(np_weight))

# Can perform element-wise calculations on height and weight
# Calcs very fast & computationally efficient, esp with 1000s of observations in data
# NOTE: each height-weight observation pairing needs to correspond with one another
    # For person A, height = 1.87 & weight = 81.65
    # Person B = 1.87 & weight = 97.52
bmi = np_weight / np_height ** 2
print(bmi)

# Can do quick subsets
# Print bmi values that are > 23
bmi[bmi > 23]


####################
##### EXERCISE #####
####################


# Convert list of weights to numpy array
# Convert all weights from kilograms to pounds
    # 2.2 lbs = 1 kg
# Print resulting array of weights in pounds

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
np_weight_kg = np.array(weight_kg)
np_weight_lbs = np_weight_kg * 2.2
print(np_weight_lbs)


##################################
##################################
##################################


# PANDAS DATAFRAMES
# Dataframes allow store and manipulate tabular data in rows (observations) and columns (variables)
# Built upon Numpy package


# Can create dataframe multiple ways
# Method 1: convert data from dictionary
import pandas as pd
dict_countries = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]}

dict_df = pd.DataFrame(dict_countries)
dict_df

# DataFrame() automatically assigns indices based on row number (starts with 0)
# Can change this
dict_df.index = ["BR", "RU", "IN", "CH", "SA"]
dict_df

# Method 2: import file
cars = pd.read_csv('cars.csv', index_col = 0)
cars

# Can index a dataframe in various ways
# Method 1: single square brackets around col name (prints data as Pandas Series)
print(dict_df['country'])

# Method 2: double square brackets around col name (prints data as Pandas DF)
print(dict_df[['country']])

# Can only print multiple cols using double brackets
print(dict_df[['country', 'capital']])

# Square brackets also used to access rows (observations)
# Print first 4 rows of dict_df
dict_df[0:4]

# Print 3rd and 4th rows
dict_df[2:4]

# Can also use loc and iloc to access rows/columns
# loc = label-based = have to specify rows/columns based on row/column names
# iloc = index-based = have to specify rows/columns based on row/column integer index

# Print data associated with row 3 (index 2)
dict_df.iloc[2]

# Print data associated with row 3 (index 2), columns 1 & 2 (indices)
# df_name = [rows, columns]
# REMEMBER: 0:2 = give me columns with indices 0 - 1; 2 is NOT INCLUSIVE
dict_df.iloc[2, 0:2]

# Print data associated with Brazil and China using their row indices
dict_df.loc[['BR', 'CH']]

# Print data associated with Brazil and China's populations using their row indices and column names
dict_df.loc[['BR', 'CH'], ['country', 'population']]


##################################
##################################
##################################


# GENERATORS
# Generators = functions which return iterable set of items, one at a time
# Used to create iterators
# Starts with a "for" statement, which then contains yield statement 
    # Yield = returns values/objects that meet criteria
    # Different from return b/c return terminates function/loop while yield only pauses it and returns back to "for" statement
# Yield and .append() act similarly but have different ways of interacting with loop and storing iterative data

# Yield Method
test_list = [1, 4, 5, 6, 7]

def print_even_yield(list_name):
    for i in list_name:
        if i % 2 == 0:
            yield i

even_numbers = [i for i in print_even_yield(test_list)]

# Append Method
test_list = [1, 4, 5, 6, 7]

even_numbers = []
def print_even_return(list_name):
    for i in list_name:
        if i % 2 == 0:
            even_numbers.append(i)

print_even_return(test_list)

# Return 7 random integers
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))


####################
##### EXERCISE #####
####################


# Write a generator to return Fibonacci series
# Calculated using the following formula:
    # first two numbers of a series is always equal to 1
    # each consecutive number returned = sum of last 2 numbers
import types
# Example of how this works found in python_learning_fibonacci_example.docx
def fib():
    a, b = 1, 1 # initial starting values: first 2 numbers of a series are 1
    while 1:
        yield a # store the initial value of "a" before calculating its new value 
        a, b = b, a + b # a becomes b, and b becomes a + b
        # After reassign a and b, rerun both functions with new a and b values

if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib(): # n = result value from fib()
        print(n)
        counter += 1 # aka counter = counter + 1
        if counter == 10: # once fib() starts running for the 10th time, stop
            break



####################
##### EXERCISE #####
####################


# For each pt_id, subset extracellular domains with >= 8 AAs
# Use yield and .append() methods

# Import test data
test_data = pd.read_csv('/mnt/users/tfloyd/continuing_ed/2024_06_17_test_dataset_extracellular_domains.txt',
                        sep = '\t')

# Group all ex_domain_seqs associated with each unique pt_id
# Store results in a dictionary
test_data_dict = {}
for id in test_data['pt_id'].unique():
    test_data_dict[id] = [test_data['ex_domain_seq'][domain] for domain in test_data[test_data['pt_id'] == id].index]

# Yield Method
def pass_yield(dict_name):
    for domain in dict_name:
        if len(domain) >= 8:
            yield domain

# Run function and calculate how long it takes to run
import time
start_time = time.time()

domains_pass_yield = {}
for id, domain in test_data_dict.items():
    domains_pass_yield[id] = [domain for domain in pass_yield(domain)]

print("--- %s seconds ---" % (time.time() - start_time))

# Append Method
def pass_append(dict_name):
    for domain in dict_name:
        if len(domain) >= 8:
            d_pass.append(domain)

# Run function
start_time = time.time()

domains_pass_append = {}
for id, domain in test_data_dict.items():
    d_pass = []
    pass_append(domain)
    domains_pass_append[id] = d_pass

print("--- %s seconds ---" % (time.time() - start_time))


##################################
##################################
##################################


# LIST COMPREHENSIONS
# Creates new list based on another list in single, readable line


# Create a list of integers which specify the length of each word in a sentence
# except for if the word is "the"
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
# Format = [returned value/object for items in items_list if condition]
word_lengths = [len(word) for word in words if word != "the"]
word_lengths


####################
##### EXERCISE #####
####################


# Using list comprehension, from the list "numbers",
# create a new list called "newlist" which contains only positive numbers
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [num for num in numbers if num > 0]


##################################
##################################
##################################


# LAMBDA FUNCTIONS
# Inline functions defined at the same place we're using it: 
# aka a function that's only going to be used once within the code
# Don't need to have a name = anonymous functions
# (In contrast to def functions: need a name in order to be called throughout code)


# Simple example adding user-defined variables
a = 1
b = 2
sum = lambda x,y : x + y
c = sum(a,b)
print(c)


####################
##### EXERCISE #####
####################


# Write a lamba fxn to check if a number in a list is odd
# For each element, print "True" if odd and "False" if not
l = [2,4,7,3,14,19]

# Method 1
for i in l:
    remainder_calc = lambda x: x % 2 > 0
    remainders = remainder_calc(i)
    print(remainders)

# Method 2
remainder_calc = lambda x: x % 2 > 0
[remainder_calc(i) for i in l]

# Method 3 (no lambda but much more simple)
[i % 2 > 0 for i in l]


##################################
##################################
##################################


# MULTIPLE FUNCTION ARGUMENTS


# Create a function "foo" that prints > 1 argument defined in the fxn
def foo(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))

foo(1, 2, 3, 4, 5)

# Can send function user-defined arguments by keyword by using **options in argument and options.get() within function
# When calling the function, order of arguments doesn't matter as long as they're defined
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))


####################
##### EXERCISE #####
####################


# Create "foo" and "bar" functions to receive ≥ 3 arguments each
# Foo: must return amount of extra arguments received
# Bar: if argument with the keyword "magicnumber" = 7, print True, otherwise False
def foo(a, b, c, *therest):
    additional_args = list(therest)
    return(len(additional_args))

def bar(a, b, c, magicnumber):
    return(magicnumber == 7)


##################################
##################################
##################################


# EXCEPTION HANDLING
# Handles programming errors
# Most errors will stop the program once the error occurs
# Sometimes, user may want to the program to continue AND return something specific related to the error(s)


# Iterate over a list that's supposed to be 20 numbers, but isn't
# If reach end of list and don't have 20 numbers, print "0" until hit 20
the_list = (1, 2, 3, 4, 5)

def do_stuff_with_number(n):
    #print("You're missing " + 20 - n + " numbers!")
    print(n)

def catch_this():
    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError: # Raised when accessing a non-existing index of a list
            do_stuff_with_number(0)

catch_this()

# Alternative method that prints number of items in list needed to reach 20
the_list = (1, 2, 3, 4, 5)
def catch_this2():
    for i in range(20):
        list_remainder = 20 - len(the_list)

        try:
            do_stuff_with_number(the_list[i])
        except IndexError: # Raised when accessing a non-existing index of a list
            print("You're missing " + str(list_remainder) + " numbers!")
            break # exit loop

catch_this2()


####################
##### EXERCISE #####
####################


# Return the last name of the actor and make sure no exceptions pass
actor = {"name": "John Cleese", "rank": "awesome"}

def get_last_name():
    return actor["name"].split(1)