"""
  Lesson 1: ex2.py
"""

# Here is my shopping list:
#
# 2.99 Apples
# 1.79 Milk
# 3.49 Bread
# 6.99 Chicken
# 2.49 Pasta

# 1. Make a python list of the 5 items above and print it out.

# INSERT YOUR CODE HERE
#Shopping_Item = ["Apples", "Milk", "Bread", "Chicken", "Pasta"]

#Apples = 2.99
#Milk = 1.79
#Bread = 3.49
#Chicken = 6.99
#Pasta = 2.49

Shopping_dict = dict(Apples=2.99, Milk=1.79, Bread=3.49, Chicken=6.99, Pasta=2.49)
#shopping_Price = [Apples, Milk, Bread, Chicken, Pasta]
#print(Shopping_list)
#print(Shopping_Item)
#print(shopping_Price)
print("Shopping Items:-", list[Shopping_dict.keys()])
#for i in Shopping_dict.keys():
#  print(i)

# 2. Use python as your calculator and print out the total cost of
#    all items on shopping list.

# INSERT YOUR CODE HERE

print("Total Cost :-", sum(Shopping_dict.values()) ) 



# 3. I have decided that we need 5 cartons of milk, can you recalculate
#    it and print it out again?

# INSERT YOUR CODE HERE
#Recalculate = (Milk * 5) + Apples + Bread + Chicken + Pasta 
#print("Recalculated Cost:-", Recalculate)

x=0
for i in Shopping_dict.keys():
    if i == "Milk":
       x += Shopping_dict[i] * 5
    else:
      x += Shopping_dict[i]
    
print("Recalculated Cost", x)
# 4. Print out every item of your shopping list on a new line.

# INSERT YOUR CODE HERE

#for i in Shopping_Item:
#  print(i, Shopping_dict[i])

for i in Shopping_dict.keys():
  print(i)