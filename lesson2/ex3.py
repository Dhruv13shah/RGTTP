"""
  Lesson 2: ex3.py
"""

# 1. Create a list containing three elements representing the
#    name, age, and occupation of a person.
#    Then, print the sentence using the elements with .format()

# INSERT YOUR CODE HERE

# my_list: list[int] = []

# for i in range(10):
#   new_list: list[int] = [i, i**2, i**3]
#   my_list.append(new_list)
# print(my_list)

#from ex4 import Values


person: list = ["Dhruv", "30", "Engineer"]
print("{} is {:+>3} year young and he is an {}".format(*person))


# 2. The dictionary should contain keys such as
#    'title', 'author', and 'publication_year'.
#    Use the .format() method with multiple positional arguments.
#    Example:
#    "The guidebook [title] by [author] was published in [publication_year]."

# INSERT YOUR CODE HERE

##converting tuple to dic for learning purpose

dir_format: dict = dict(title="RAMAYAN", author="Valmiki", Publication_year="00")

print("The guidebook {} by {} was published in {}.".format(*dir_format.values()))

# 3. The dictionary should hold details about a spaceship, such as
#    'name', 'type', and 'purpose'.
#    Use the .format() method with named arguments.
#    Example:
#    "The spaceship is called the [name]. It is a [type] used for [purpose]."

# INSERT YOUR CODE HERE

ship_detail: dict = {"name": "mangalyan", "type": "PSLV", "purpose": "Study Martian Atmosphere"}

print("The spaceship is called the {name}. It is a {type} used for {purpose}.".format(**ship_detail))

## using % operator ## Need to work more on this to correct it.

#print(The spaceship is called the %(name). It is a %(type) used for %(purpose).".format(**ship_detail))

## using f-strring

#print(f"The spaceship is called the {ship_detail['name']}. It is a {ship_detail['type']} used for {ship_detail['purpose']}.") 