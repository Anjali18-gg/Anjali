# ---- mymodule.py (custom module) ----
def add(a, b):
    return a + b

def sub(a, b):
    return a - b


# ---- main program ----
import mymodule

x, y = 10, 5
print("Addition:", mymodule.add(x, y))
print("Subtraction:", mymodule.sub(x, y))
