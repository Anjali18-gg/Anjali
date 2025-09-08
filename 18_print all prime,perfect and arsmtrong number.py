# Program to print all Prime, Perfect, and Armstrong numbers in a given range

# Function to check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check perfect number
def is_perfect(n):
    if n < 2:
        return False
    sum_divisors = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors == n

# Function to check Armstrong number
def is_armstrong(n):
    num_digits = len(str(n))
    return n == sum(int(digit) ** num_digits for digit in str(n))

# Taking range input
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

primes = []
perfects = []
armstrongs = []

for num in range(start, end + 1):
    if is_prime(num):
        primes.append(num)
    if is_perfect(num):
        perfects.append(num)
    if is_armstrong(num):
        armstrongs.append(num)

print("\nPrime numbers in range:", primes)
print("Perfect numbers in range:", perfects)
print("Armstrong numbers in range:", armstrongs)
print("This code is written and executed by Anjali_0231BCA188")
