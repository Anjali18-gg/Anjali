  # Fibonacci using simple function (iteration)
def fibonacci_iter(n):
    a, b = 0, 1
    print("Fibonacci series (Iterative):")
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
    print()


# Fibonacci using recursion
def fibonacci_rec(n):
    if n <= 1:
        return n
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


# Main Program
num = int(input("Enter a number: "))

# Iterative approach
fibonacci_iter(num)

# Recursive approach (generate and print series)
print("Fibonacci series (Recursive):")
i = 0
while True:
    fib = fibonacci_rec(i)
    if fib > num:
        break
    print(fib, end=" ")
    i += 1

print("This code is written and executed by Anjali_0231BCA188")
