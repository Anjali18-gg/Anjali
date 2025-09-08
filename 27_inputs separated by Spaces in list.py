# ----- Multiple Inputs (Strings) -----
name, city = input("Enter your name and city (separated by space): ").split()
print("Name:", name)
print("City:", city)

# ----- Variable Number of Inputs -----
words = input("\nEnter some words (separated by space): ").split()
print("Words List:", words)

# ----- Multiple Integer Inputs -----
numbers = list(map(int, input("\nEnter integers separated by space: ").split()))
print("Numbers List:", numbers)
print("Sum of Numbers:", sum(numbers))
print("This code is written and executed by Anjali_0231BCA188")
