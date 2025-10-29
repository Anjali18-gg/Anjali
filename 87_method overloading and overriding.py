# Demonstrate Method Overloading and Overriding

class MathOperation:
    # Method Overloading using default arguments
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            print("Adding three numbers:", a + b + c)
        elif a is not None and b is not None:
            print("Adding two numbers:", a + b)
        else:
            print("Single value:", a)

# Child class to demonstrate Method Overriding
class AdvancedMathOperation(MathOperation):
    def add(self, a=None, b=None, c=None):
        print("Overridden method in child class")
        super().add(a, b, c)  # Optionally call parent method

# Creating objects
parent_obj = MathOperation()
child_obj = AdvancedMathOperation()

# Method Overloading demonstration
print("=== Method Overloading ===")
parent_obj.add(5)
parent_obj.add(5, 10)
parent_obj.add(1, 2, 3)

# Method Overriding demonstration
print("\n=== Method Overriding ===")
child_obj.add(4, 6)
