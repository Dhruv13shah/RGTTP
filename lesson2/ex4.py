"""
  Lesson 2: ex4.py
"""

# 1. Print the formatted keys and values of the dictionary.
#    versions: dict[str, int] = {'Stein': 15, 'Train': 16, 'Wallaby': 17}

# INSERT YOUR CODE HERE

versions: dict[str, int] = {'Stein': 15, 'Train': 16, 'Wallaby': 17}

print("Printing the version number {} {} {}".format(*versions.values()))
print("Printing the version name {} {} {}".format(*versions.keys()))
# 2. Print {} around the version numbers.

# INSERT YOUR CODE HERE
print("Printing the version Number {{{}}} {{{}}} {{{}}}".format(*versions.values()))
# 3. Print numbers in decimal, byte and hexadecimal form.

# INSERT YOUR CODE HERE

print("Printing the version number in decimal {:d} {:d} {:d}".format(*versions.values()))
print("Printing the version number in byte {:b} {:b} {:b}".format(*versions.values()))
print("Printing the version number in Hexadecimal {:x} {:x} {:x}".format(*versions.values()))
