"""
  Lesson 3: ex4.py
"""

# 1. Create your own Shopping List type.
#
# a. Initialize the ShoppingList class with shopping_list
#    shopping_list = ['apples', 'milk', 'bread', 'carrot', 'pasta']
#
# b. Add in_list method, that checks if the item is in list or not,
#    use the format() or f-strings to return the string based on truth:
#    - 'apples' is in the shopping list.
#    - 'apples' not in the shopping list.
#
# c. Add special function when printing the list to output:
#    * Replace the list with {} and print using format().
#    My shopping list: ['apples', 'milk', 'bread', 'carrot', 'pasta']
#
# d. Add special function for comparison of two objects to output:
#    * Based on the truth.
#    - True
#    - False

# INSERT CODE HERE
class ShoppingList(object):
  def __init__(self) -> None:
      self.shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']

  def in_list(self, item):
    if item in self.shopping_list:
      return f"{item} is in shopping list"
    else:
      return f"{item} is not in shopping list" 

monday: ShoppingList = ShoppingList()
print(monday.shopping_list)      
print(monday.in_list('apples'))
print(monday.in_list('banana'))