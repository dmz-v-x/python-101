# This is a single line comment

# This is
# a 
# Multi-line comment

"""
This is
also a 
multi-line comment
using triple quotes
"""

'''
This is also a 
multi-line comment
'''

# This """""" & '''''' are called docstring used inside a class or a function we can access the docstring of a class or a function using:
# print(<function/class name>.__doc__)

# Example: Function to add two numbers

def add(x, y):
  """This function adds two number"""
  return x + y;

sum = add(5, 5);
print("The sum of x and y is", sum)
print(add.__doc__)






