# Program to print all Perfect numbers between 1 and 2025

def is_perfect(n):
    if n < 2:
        return False
    sum_divisors = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors == n

perfect_numbers = []

for num in range(1, 2026):
    if is_perfect(num):
        perfect_numbers.append(num)

print("Perfect numbers between 1 and 2025 are:", perfect_numbers)
print("Total count:", len(perfect_numbers))
print("This code is written and executed by Anjali_0231BCA188")
