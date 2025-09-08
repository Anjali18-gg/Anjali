# Program to check if a number is an Armstrong number

# Taking input from the user
num = int(input("Enter a number: "))

# Find the number of digits
num_digits = len(str(num))

# Calculate sum of digits raised to the power of num_digits
sum_of_powers = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** num_digits
    temp //= 10

# Check Armstrong condition
if num == sum_of_powers:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
print("This code is written and executed by Anjali_0231BCA188")
