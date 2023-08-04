"""
  Lesson 2: ex2.py
"""

# 1. Use string formatting with empty curly brackets {}
#    to take the argument passed into format and print a
#    sentence of your choice.

# INSERT YOUR CODE HERE

var1: str = "formatting"

print("This is a sentence which use the string {}".format(var1))

# 2. Use string formatting with positional arguments and
#    print the sentence: "Don't Panic!"

# INSERT YOUR CODE HERE
print("{1} {0}".format("panic","Don't"))

# 3. Use string formatting with named arguments and
#    print the sentence: "[name] is really [what]!" and
#    fill in the brackets with your name and "great".

# INSERT YOUR CODE HERE

name : str = "Dhruv"
what : str = "great"

print("{} is really {}!".format(name, what))