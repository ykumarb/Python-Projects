# int num = 123
# str my_str = 'Hello'
# bool boolean = False
# float val = 3.22
# str str1 = "3"
# str str2 = '1'

# Datatypes and variables
name = 'Yupindra'
print(name)
name = 'Kamalesh'
print(name)
age = 18
print(age)
age = 20
print(age)
_name = "Yupindra"
print(_name)
NAME = "Joseph Kurvila"                     
print(NAME)

# input
print("What is your name ?")
name = input()
print("Your name is " + name)

print("What is your Naitve ?")
native = input()
print("My native is", native)


# operators
num1 = 67
num2 = 67
print(num1 + num2)
print(num1 - num2)
print(num1*num2)

# exponents - **
# integer division - //
# modulo - %

num1 = 56
num2 = 64
print(num1**num2)
print(num1//num2)
print(num2%num1)

# Both inputs, variables and operators
print("Pick a number: ")
num1 = input() # Gives a type of string
print(type(num1))

print("Pick another number: ")
num2 = input() # Gives a type of string
print(type(num2))


SUM = int(num1) + int(num2) # Convert a type string to int using casting type
print(type(SUM))
print("Sum is:",SUM)

# Relational operators
# >
# <
# ==
# !=

# Assignment operator

# =

# Examples of relational operators
print(2 < 3)

print(2 > 3)

print(4 != 5)

print("Hellow" != "Hello")

print("hello" != "Hello")

print('hello' != "hello")

print("hello" != 'hello')

print("hello" == "hello")

print("hello" == "Hello")

print('hello' == "hello")

print(2-3+4)


# Conditionals
# Check if a person is eligible to vote
print("Enter the age of a person: ")
age = int(input())
print("Type of age after retreive is:", type(age))
print("Age is:",age)

if age >= 18:
    print("Person is eligible to vote!!")
else:
    print("Person is not eligible to vote!!")


# Chain condiitonal/Nested statements and logical operators
x = int(input())
y =int(input())

if x == 1 and x + y == 91:
   print("X is 1 and x+y is 91")
elif x > 1 and not(x + y == 91):
    if x is 5:
        print("X is 5 but x+y is not 91")
    else:
        print("x is > 1 and x+y is not 91") 
else:
    print("x and x+y satisfies")

# Loops - For
# Write a loop logic to print the multiples of 2 without 09
for num in range(0,10,2):
    if num is not 0:
        print(num)

# Loops - while

loop = True

while loop:
    print("Enter the code: ")
    code = input()
    if code == "stop":
        loop = False
        break # optional not needed since we reset loop to break loop


# List's and Tuples
# List
# Iteraing item or iterating through a list

print("-------------------------------")
fruits = ['Apple', 'Orange', 'Grapes', 4]
print(fruits)
print("Type is:",type(fruits))

cnt = 0
for fruit in fruits:
    if type(fruit) is not str:
        print("Fruit item is not string, it is of type",type(fruit),fruit,"invaid!!!!")
        break
    else:
        cnt += 1
        print("fruit",cnt,":",fruit)

print("Total number of fruit items in the list is",cnt)

# Append it to fruit list 

fruits.append('Pear')
print(fruits)
fruits.append('srawberry')
fruits.append('Blueberry')
print(fruits)

fruits[5] = 'Butter'
print(fruits)

# Different way to manipulate the list
cnt = 0
only_fruits = fruits
for x in range(len(fruits)):
    if type(fruits[x]) is not str:
        print("Fruit item is not string, it is of type",type(fruit),fruit,"invaid!!!!")
        print("Index of invalid item:",x)
        remove_item_from_idx = x
        only_fruits[x] = ""
        #remove_fruit = only_fruits[x]
        #only_fruits.remove()
    else:
        cnt += 1
        print("fruit",cnt,":",fruit)

print(only_fruits)


# Tuples
color = (0,255,255)
subjects = ('Math', 'Science', 'Social', 'History')
print(type(subjects))



# String methods

# .strip() .len() .upper() .lower() .split()

print("Provide an input")
data = input()
print(data.strip())
print(len(data)) # Get the length of the string with the trailing and leading whitespaces
print(len(data.strip())) # Strip the leading and trailingthe whitespaces and then get the length
print(data.upper()) # Convert a string to upper case letters
print(data.lower()) # Convert a string to lower case letters
print(data.split(':')) # By default the delimiter is space 

# Splice operator working

games = ['GTA', 'Moto', 'Vice City']
gstring = 'GTA is better than Moto?'

print(games[0:3:2]) # Slice operation has start, stop and step
print(gstring[0:4:5]) 

# Insert item using slice operator

books = ['Science', 'Physics', 'Chemistry', 'Organic Chemistry']

books[2:2] = "Social" # Inserts social in 2nd index(different behavior when printed)

print(books)

# Functions
def average():
    sum = 0
    len = 0
    for i in range(0,10):
        sum += i
        len +=1
    # print("Sum:",sum,"Len:",len)
    return(sum/len)

print("Average is:",average())
print("Approximated average:",int(average()))

# How to read from a file
file = open('file.txt', 'r')
read_lines = file.readlines()
file.close()
new = []
for line in read_lines:
    if line[-1] == '\n': # Other ways to do is strip simply with no arguments to remove \n
        new.append(line[:-1])
    else:
        new.append(line)

print(new)

# Writing to a text file
file = open('file.txt', 'w')
file.write('Python is here!!!\n')
file.write('Yes it is !!')
file.close()

# Using .count and .find methods
string = 'Harry Potter'
print(string.find('r')) # It gives the first occurence of a string's index
print(string.count('r')) # It gives the count of the string provided as a argument


# Introduction to modular programming
import os
import pygame
import math

print(math.sqrt(25))
print(math.pi)
print(math.radians(math.pi))


# optional parameters (advanced functions)

text = 'String is there'

def grepper(text='Yupindra'):
    if 'String' in text:
        print("String is there in text")
    else:
        print("String is not there in text")

grepper()