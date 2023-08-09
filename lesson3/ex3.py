"""
  Lesson 3: ex3.py
"""

# Here is my shopping list:
from audioop import reverse


shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']

# 1. Sort the list using built-in function sorted() and print that list

# INSERT CODE HERE

sorted_list= sorted(shopping_list)
print("Sorted Values using function:-", sorted_list)
# 2. Sort the list using .sort() method and print that list

# INSERT CODE HERE
shopping_list.sort()
print("Sorted Values :-", shopping_list)

# 3. Use the built-in function reversed(), reverse the list and print that list

# INSERT CODE HERE
##not working

reversed_function: list[str] = list[reversed(shopping_list)]
print("reversed Values :-", reversed_function)

# 4. Reverse the list using sort() method and print the list

# INSERT CODE HERE
reversed_method=shopping_list.sort(reverse=True)
print("reversed Values :-", reversed_method)

# 5. Reverse the list using sorted() method and print the list

# INSERT CODE HERE
reverse_sorted= sorted(shopping_list,reverse=True)
print("reverse sorted:- ", reverse_sorted)
