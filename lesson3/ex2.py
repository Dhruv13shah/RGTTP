"""
  Lesson 3: ex2.py
"""

# 1. Create a list of number 0 to 9 using a for loop.
#
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# INSERT CODE HERE

## Method 1 ##

# list_of_number: list[int] = [i for i in range(10)]
# print("List of number:-",list_of_number)

## method 2 ##

numeric_numebrs: list[int] = []
for i in range(10):
  numeric_numebrs.append(i)
print("List of numeric number:", numeric_numebrs)


# 2. Create a list of number from 0 to 9 the power of 2 using a for loop.
#
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# INSERT CODE HERE

power_of_number=[i**2 for i in range(10)]
print("power of numbers are:-", power_of_number)

# 3. Create a list of lists, which contains elements that are
# number, number(to the power of 2), number(to the power of 3)
#
# [[0, 0, 0], [1, 1, 1], [2, 4, 8], [3, 9, 27], [4, 16, 64],
#  [5, 25, 125], [6, 36, 216], [7, 49, 343], [8, 64, 512],
#  [9, 81, 729]]
### Method-1 Not working As of now

# list_of_list=[ i**3 for i in range(10) ]
# print("Printing the list of list", list_of_list)

### Method -2 
my_list: list[int] = []
for i in range(10):
  new_list: list[int] = [i, i**2, i**3]
  my_list.append(new_list)
print(my_list)

# INSERT CODE HERE

# 4. Add condition in a for loop, that only numbers that are odd are added.
#
# [[1, 1, 1], [3, 9, 27], [5, 25, 125], [7, 49, 343], [9, 81, 729]]

# INSERT CODE HERE
# my_list: list[int] = []
# for i in range(10):
#   if i % 2 != 0:
#      new_list: list[int] = [i, i**2, i**3]
#      my_list.append(new_list)
# print(my_list)

odd_list: list[int] = [[i , i**2, i**3]for i in range(10) if i % 2]
print("odd_list:- ", odd_list)
# 5. Create a nested lists in a list with a for loop:
# [['ax', 'bx', 'cx', 'dx', 'ex'],
#  ['ay', 'by', 'cy', 'dy', 'ey'],
#  ['az', 'bz', 'cz', 'dz', 'ez']]

# list1: list[str] = ['a','b','c','d','e']
# list2: list[str] = ['x','y','z']
# netsted_list: list[list[str]] = []
# netsted_list1: list[str] = []

# for i in list2:
#   temp_list: list[str] = []
#   for j in list1:
#     temp_list.append(j+i)
#   print(netsted_list1)
#   netsted_list.append([temp_list])   
# print("nested list:", netsted_list)    

nested_method: list[list[str]] = [[j+i for j in 'abcde'] for i in 'xyz']
print(nested_method)