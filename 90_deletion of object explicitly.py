class MyClass:
 def __init__(self, value):
     self.value = value
obj1 = MyClass(10)
obj2 = obj1 # Increase reference count
del obj1 # Decrease reference count but obj2 still references the object
del obj2 # Now the reference count is zero, object is destroyed
