# CHAPTER 1 - THE BASICS
# Lesson 1.3 - Strings

# This lesson is going to focus on Strings and what you can do with them

# You can add strings together with +
'hello' + ' world' == 'hello world' 

# You can index into strings to get the Nth character
'abc'[1] == 'b'

# You can find the length of a string using the len() function
len('abc') == 3

# You can slice into strings to get the characters from N to M (not including the character at M)
print('abc'[1:3]) # this prints 'bc' since it stops at index 3, which is the end of the word
print('abc'[1:1]) # this prints the empty string '' since it starts at index 1 but also ends there
print('abc'[3:1]) # this also prints the empty string since 3 > 1

# ---
# ASSIGNMENT: SLICING
# ---

# TODO: Modify ONLY the numbers in the following code to make it print hello world
print('this should print hello world sometime'[0:0])


# ---
# SPECIAL CHARACTERS
# ---

# Since strings are declared via quotes, you have to use a special "escape character" to create a string with a quote in it
# The backslash \ is this escape character.

print('\'This is a string surrounded by single quotes\'')
'\" this string is surrounded by double quotes \"'
"\" remember that strings can also be declared using double quotes \""

# There are also some whitespace characters you can declare using the backslash- most notably, the newline character
# The newline character is a special character that tells the computer you want a new line- like pressing enter
# To display this in strings, we use \n, the newline character

print('This is one line \n this is another')

# The most useful escape characters are:
# \' single quote
# \" double quote
# \n newline
# \t tab
# \\ backslash

# ---
# STRING METHODS
# ---
# There are various method you can call on strings

print('jan'.capitalize()) # this prints Jan, as it capitalizes the string
print('jan'.upper()) # this prints JAN
print('JaN'.lower()) # this prints jan
print('jan  '.strip()) # this prints jan as it removes all beginning and trailing whitespace (spaces and tabs and newlines)

'a, b, c'.split() == ['a', 'b', 'c']

# There's a lot more! Check out https://www.w3schools.com/python/python_ref_string.asp

# ---
# FSTRINGS
# ---

# When you want to display strings with lots of changing bits to them it can be annoying and inefficient 
# to chain together a bunch of additions with +

# Instead you can use an FString. Putting an f before a quote turns the string into an fstring.

f'This is an fstring'

# FStrings allow you to put arguments in curly braces {} which are then printed as strings

f'This is an fstring with arguments {"jan"} and {"nicole"}'

# They can hold any inputs. For example:

f'The number one is {1}' == 'The number one is 1'

# Whereas a regular string would just display {1} with the curly braces

print('The number one is {1}')

# You can still have curly braces in text in fstrings by doubling them

f'This fstring has {{ and }}' == "This fstring has { and }"

# ---
# CONSOLE INPUT
# ---

# When you run a python script, you can get input from the console using the input() function
input()
input('You can put a message here: ')

# input is a function that returns a string. You can use string methods on it. For example:
print(input().upper()) # this prints whatever you put in input in ALL CAPS

# ---
# ASSIGNMENT: PRINT THE NAME
# ---

# TODO: Write code that asks for the users name, and then says
# Hello "name"!
# Where name is whatever name they inputted. Include the quotes!