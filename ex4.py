"""
  Lesson 1: ex4.py
"""

# 1. Create a new list with the following values:
#    Apple, Milk, Bread, Chicken and Pasta

# INSERT YOUR CODE HERE

Shopping = ["Apple", "Milk", "Bread", "Chicken", "Pasta"]

# 2. Write a check to see if Orange is in the shopping list or not.

# INSERT YOUR CODE HERE

#if 'orange' in Shopping:
#    print("orange is in shopping list")
#else:
#    print("orange is not in shopping list")


    
     
# 3. Write a function "in_shopping_list" that takes a item such as
#    orange, and returns True or False.
#    Depending whether the item is in the list or not.

# INSERT YOUR CODE HERE
def in_shopping_list(item):
  #Shopping.append("Orange")
  #print(Shopping)
  if item in Shopping:
    return True  
  else: 
    return False  


print(in_shopping_list("Orange"))

# 4. Write a function "show_shopping_list" that will return a
#    shopping list and print it out on the screen.

# INSERT YOUR CODE HERE
def show_shopping_list():
  return Shopping

print(show_shopping_list()) 
# 5. Create a list of the following values: 2.99 1.79 3.49 6.99 2.49

# INSERT YOUR CODE HERE
Values = [2.99, 1.79, 3.49, 6.99, 2.49]
# 6. Create a function price_checker, and pass this list as
#    an argument and let the function return the cheapest price.#

# INSERT YOUR CODE HERE
def price_checker(price):
    return min(price)

print("Cheapest", price_checker(Values))    
# 7. Write another function show_price, that will call your
#    price_checker function and uses the result to
#    print the cheapest price.

# INSERT YOUR CODE HERE

def show_price(cheap_price):
  result = price_checker(cheap_price)
  print("Function call :- ", result)

show_price(Values) 