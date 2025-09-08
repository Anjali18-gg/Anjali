# ----- Multiple Inputs (Strings) -----
name, city = input("Enter your name and city (separated by space): ").split()
print("Name:", name)
print("City:", city)

# ----- Variable Number of Inputs (Strings, no list) -----
print("\nEnter some words (separated by spaces): ")
for word in input().split():   # directly looping over words
    print("Word:", word)

# ----- Multiple Integer Inputs (no list) -----
print("\nEnter numbers (separated by spaces): ")
total = 0
for num in input().split():
    n = int(num)     # convert each input to integer
    print("Number:", n)
    total += n
print("Sum of numbers:", total)

print("this program is written and excecuted by Anjali_0231BCA0188")

