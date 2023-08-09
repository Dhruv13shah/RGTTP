"""
  Lesson 3: ex1.py
"""

# Here is my shopping list:
shopping_list: list[str] = ['apples', 'milk', 'bread', 'carrot', 'pasta']

# 1. Add banana to a shopping list.

# INSERT CODE HERE

shopping_list.append("banana")
print("Adding banana to the shopping list.",shopping_list )

# 2. Add chocolate in the third position in your shopping list

# INSERT CODE HERE

shopping_list.insert(2,"chocolate")
print(shopping_list)

# 3. Extend shopping list by the following items:
# ['chocolate', 'carrot', 'avocado']

# INSERT CODE HERE

extended_shopping_list: list[str] = ['chocolate', 'carrot', 'avocado']
shopping_list.extend(extended_shopping_list)

print("Extended Shopping List:-", shopping_list)
# 4. Remove first chocolate only

# INSERT CODE HERE

shopping_list.pop(3)
print("Removing first chocolate from Shopping List:-", shopping_list)

# 5. Remove last item from the list

# INSERT CODE HERE
shopping_list.pop()
print("Removing last item from Shopping List:-", shopping_list)

# 6. Remove third item from the list

# INSERT CODE HERE

shopping_list.pop(3)
print("Removing third item from Shopping List:-", shopping_list)


# 7. Count how many carrots are in the shopping list?

# INSERT CODE HERE

number_of_carrot=shopping_list.count('carrot')
print("Counting the carrots:-", number_of_carrot)

# 8. Get the index of the chocolate (careful can throw traceback)

# INSERT CODE HERE

index_of_chocolate=shopping_list.index('chocolate')
print("Index of the chocolate:-", index_of_chocolate)
# 9. Get the index of carrot, make sure this code is executed

# INSERT CODE HERE
index_of_carrot=shopping_list.index('carrot')
print("Index of the carrot:-", index_of_carrot)