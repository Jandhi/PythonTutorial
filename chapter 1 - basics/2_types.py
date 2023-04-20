# CHAPTER 1 - THE BASICS
# Section 1.2 - Types

from imports.firstcode import *
# you can ignore this line
# I will explain imports later- they just give us some helpful code

# ---
# TYPES
# ---

# Python code has a few different basic types, which are different forms of data
# For example, you have already learned about strings, which are lines of text
'this is a string'

# We will be covering all the basic types in this lesson
# Don't worry too much about the details if some of the types confuse you. 
# We will be covering each in more detail later.

# There are also numbers. Most numbers have the "int" type, which means integer, which is any number without a decimal.
1 # this is an integer
2415 # so is this
243535635123412446362 # also an integer
-8 # integers can be negative
0 # or zero

# you can put underscores in between digits for clarity; python will ignore them
1_000_000
1000000 # this is the same as the above

# Numbers with decimals have the "float" type. This refers to their full name as "floating point" numbers, which is just how the decimal is stored.
1.1 # this is a float 
0.65 # this is also a float
2.2592 # so is this

# NOTE: Because of how they are stored, math with floats can sometimes have rounding errors. 
print(1.0 / 3.0 * 10.0 / 3.0 * 9.0) # We would expect this to print 10.0, but it prints 9.999999999999998 due to rounding errors.

# "bool" types, or "booleans", store truth values. They can be "True" or "False"
True # this is a bool
False # this is also a bool
# There are no other bools

# There is a special object to signify the absence of data
# In other languages it is known as "null" or "nil", but in python it goes by "None"
None 

# ---
# LISTS
# ---

# There are also some more complicated types that store other types. The most basic of these is known as a list:
[1, 2, 3] # this is a list storing the numbers 1, 2, and 3.
['hello', 'world'] # this is a list storing the strings "hello" and "world"
[1, 'hello'] # you can have multiple types in a list
['hello', 1] # this is considered not equal to the above, because the order of items matters
[1, 1, 1] # a list can have duplicate values

# You can also declare a list over multiple lines
[
    1,
    2,
    3, # the last comma is optional
]

# Lists can also hold lists
[[1, 2, 3], [4, 5, 6]]

# Lists are useful when you have an ordered set of items, like a grocery list
[
    'apples',
    'orange',
    'bananas',
]

# We will touch on lists with more detail later in this chapter

# ---
# DICTIONARIES
# ---

# Another useful type is a "dict", which is short for "dictionary". 
# Just like how you may look up the definition of a word in a dictionary, it lets you look up data corresponding to any "key"
# The "key" is like the word you are looking up, while the "value" is its definition


{
    'stupendous' : 'ausing astonishment or wonder', # the colon breaks up the key and the value
    'sublime' : ' to cause to pass directly from the solid to the vapor state and condense back to solid form',
}

# dicts can associate any keys and value types, except that there can be no duplicate keys
# just like how in a dictionary you wouldn't have more than one entry
# in that way, its pretty much a ledger where you can store data for multiple categories

{
    'jan\'s bank account' : 69, # the key is "jan's bank account", the value is 69
    'nicole\'s bank account' : 1_000_000_000,
}

# We will cover dictionaries in a later chapter

# ---
# SETS
# ---

# A rarer type that is similar to lists and dictionaries is a "set"
# Like a list, it stores a bunch of items
# Unlike a list, it cannot have duplicates, and it does not care about order

{0, 1, 2}
{2, 1, 0} # this is considered equal to the set above

# NOTE: Because dictionaries and sets are initialized similarly, the empty {} is tricky. It is considered to be an empty dictionary.
# If you want an empty set, you must use set()
{} # this is an empty dictinoary
set() # this is an empty set

# We will cover sets in a later chapter

# ---
# FUNCTIONS
# ---

# Functions are procedures that do things
# You already know one of these! It's called "print"
print # this is a function

# usually, you'll be "calling" functions, which means you make them do things
# in order to call a function, you need to add parentheses after it
print() # this is calling print. (Because it has no arguments, it prints an empty line) 

# functions can also be called with arguments, which means you give them some input that they can use to do stuff
print('hello world')

# functions can also give things back to you when you call them


# the print function isn't meant to return something, so it returns None
print(print()) # this will first print an empty line, and then print None, since the inner function call returns None

# don't worry if functions inside functions is confusing to you. We will cover functions in more detail soon.

# ---
# OBJECTS
# ---

# Objects are more complicated collections of data
# I defined a Student object in a different file. We're calling him michael.
michael

# Objects can have "fields", which are pieces of associated data 
# This depends on how the object was originally defined
# For our student, I defined it with a name. We access fields using a period.
michael.name # this is michael's name
print(michael.name) # This prints "Michael"

# Objects can also have "methods", which are functions that are specific to that object
# Just as with fields, we must define these methods
# I already added a method called introduce:
michael.introduce # this is the method

# Just as with functions, we can call it with brackets.
michael.introduce() # This print "Hi I'm Michael!"

# Objects are quite complicated, so we will dedicate chapter 2 to dealing with them