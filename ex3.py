"""
  Lesson 1: ex3.py
"""

# 1. Print out your favourite food 42 times using * operator.

# INSERT YOUR CODE HERE
print("Apple"*42)

# 2. Insert space between each output and print it out again.

# INSERT YOUR CODE HERE
print("Apple "*42)

# 3. Save your favourite food into a variable and print it out 42 times

# INSERT YOUR CODE HERE

MyFavourite_Food = "Apple " 

print(MyFavourite_Food*42)

# 4. My favourite food is "sushi", save it into a variable and using
#    fast swapping operation change it with your variable.
#    Now your favourite food should be "sushi" and mine will be yours.#

# INSERT YOUR CODE HERE

Robins_fav = "sushi"
MyFavourite_Food, Robins_fav = Robins_fav, MyFavourite_Food
print("MyFavourite_Food:-", MyFavourite_Food)
print("Robins_fav:-", Robins_fav)

