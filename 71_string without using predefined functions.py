# Program to reverse a string without using predefined functions

# Input string
string = input("Enter a string: ")

reversed_string = ""

for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]

# Output
print("Reversed string:", reversed_string)
print("This code is written and executed by Anjali_0231BCA188")

