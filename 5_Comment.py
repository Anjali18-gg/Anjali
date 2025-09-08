#demonstrating comments and documentation in python

"""
This script provides example of single-line comments, multi-line comments, and docstrings.
"""

def add(a, b):
    """
Returns the sum of a and b.

Parameters:
a (int, float): First number.
b(int, float): Second number.

Returns:
int, float: Sum of a and b.
"""
    return a + b

def subtract(a, b):
    """
Returns the difference of a and b.

Parameters:
a(int, float): First number.
b(int, float): Second number.

Return:
int, float: Difference of a and b.
"""
    return a - b

#Main part of the script
if __name__ == "__main__":
    x,y = 10, 5   #Initialize variables

    #perform operations and print results
    print(f"The sum of {x} and {y} is {add(x, y)}")  #Addition
    print(f"The difference between {x} and {y} is {subtract(x, y)}")  #Subtraction 

   
