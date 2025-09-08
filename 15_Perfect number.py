# Function to check Perfect Number
def is_perfect(num):
    if num < 1:
        return False
    
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    
    return sum_of_divisors == num


# Input from user
n = int(input("Enter a number: "))

if is_perfect(n):
    print(f"{n} is a Perfect Number")
else:
    print(f"{n} is NOT a Perfect Number")
print("This code is written abd executed by Anjali_0231BCA188")    
