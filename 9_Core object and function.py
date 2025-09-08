# Demonstrating Core Objects and Functions in Python

# ----- Numbers -----
a = 10        # integer
b = 3.5       # float
c = 2 + 3j    # complex number

print("Numbers:")
print("a =", a, "| type:", type(a))
print("b =", b, "| type:", type(b))
print("c =", c, "| type:", type(c))
print()

# ----- Strings -----
s = "Hello Python"
print("String:")
print("s =", s)
print("Length of s:", len(s))
print("Uppercase:", s.upper())
print("Substring (0:5):", s[0:5])
print()

# ----- Lists -----
my_list = [1, 2, 3, 4, 5]
print("List:")
print("my_list =", my_list)
print("Length:", len(my_list))
print("Sum:", sum(my_list))
print("Max:", max(my_list))
print("First element:", my_list[0])
print()

# ----- Tuples -----
my_tuple = (10, 20, 30)
print("Tuple:")
print("my_tuple =", my_tuple)
print("Type:", type(my_tuple))
print("Second element:", my_tuple[1])
print()

# ----- Dictionaries -----
my_dict = {"name": "Anjali", "age": 22, "city": "Delhi"}
print("Dictionary:")
print("my_dict =", my_dict)
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Access by key (name):", my_dict["name"])
print()

# ----- Sets -----
my_set = {1, 2, 3, 3, 4}
print("Set (no duplicates):", my_set)
print("Length of set:", len(my_set))
print()

# ----- range() demonstration -----
print("Range from 1 to 5:", list(range(1, 6)))
print("This code is written and executed by Anjali_0231BCA188")
