class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

# Creating objects
s1 = Student("Anjali", 85)
s2 = Student("Rahul", 90)

# Accessing properties through methods
s1.display()
s2.display()
