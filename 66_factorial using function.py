def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Taking input from user
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")

print("This code is written and executed by Anjali_0231BCA188")
