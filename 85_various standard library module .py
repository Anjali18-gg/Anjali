# Demonstration of various standard library modules in Python

import math
import datetime
import random
import os
import sys

print("=== Demonstration of Standard Library Modules ===\n")

# --- math module ---
print("1. math Module:")
print("Square root of 25:", math.sqrt(25))
print("Factorial of 5:", math.factorial(5))
print("Value of pi:", math.pi)
print()

# --- datetime module ---
print("2. datetime Module:")
current_time = datetime.datetime.now()
print("Current Date and Time:", current_time)
print("Today's Date:", datetime.date.today())
print()

# --- random module ---
print("3. random Module:")
print("Random number between 1 and 10:", random.randint(1, 10))
print("Random choice from list:", random.choice(['Apple', 'Banana', 'Mango', 'Orange']))
print()

# --- os module ---
print("4. os Module:")
print("Current Working Directory:", os.getcwd())
print("List of files in current directory:", os.listdir())
print()

# --- sys module ---
print("5. sys Module:")
print("Python Version:", sys.version)
print("Platform:", sys.platform)
print()

print("=== End of Demonstration ===")
