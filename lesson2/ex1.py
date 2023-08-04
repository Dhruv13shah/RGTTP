"""
  Lesson 2: ex1.py
"""

# 1. Create a format string to display the name and age of a person.

# INSERT YOUR CODE HERE

name: str = "Dhruv"
age: int = "30"

#print("My name is {0}, I am {1} years yong".format(name,Age))
#print("My name is {0} :- {{}}".format(name,age))


def display_person(name: str,age: int) -> str:
  return(f"My Name is {name} and I am {age} Years old")

print(display_person(name, age))
# 2. Print version with it's corresponding upstream codename,
#    and use padding aligned format to left, centre and right.

# INSERT YOUR CODE HERE

ver: int = 17.2
codename: str = "wallaby"


def padding(ver: int, codename: str):
  print("{1} is on {0:>10}!".format(ver,codename))
  print("{1} is on {0:->+10}!".format(ver,codename))
  print("{1} is on {0:-=+10}!".format(ver,codename))
  

padding(ver, codename)
# 3. Show different representations of an integer.

# INSERT YOUR CODE HERE

integer_rep: int = 20

def different_rep(integer_re: int):
  print("Integer in Binary form :- {:#10b}".format(integer_re)) 
  print("Integer in Binary form :- {:#010b}".format(integer_re))
  print("Integer in Decimal form :- {:d}".format(integer_re))
  print("Integer in Octal form :- {:o}".format(integer_re))

different_rep(integer_rep)
# 4. Format a floating-point number with fixed precision.

# INSERT YOUR CODE HERE

float_point: float = 24.234

def float_precesion(float_point: float):
  print("Floating precision{:.2f}".format(float_point))

float_precesion(float_point)