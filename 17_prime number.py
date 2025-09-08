# Program to check if a number is prime

num = int(input("Enter a number: "))

# 0, 1, and negative numbers are not prime
if num <= 1:
    print(num, "is not a prime number")
else:
    # Check divisibility
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
print("This code is written and executed by Anjali_0231BCA188")        
