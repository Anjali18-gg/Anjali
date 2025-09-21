# Function to check if a number is Armstrong
def is_armstrong(num):
    order = len(str(num))
    sum_of_powers = sum(int(digit)**order for digit in str(num))
    return num == sum_of_powers

# Input range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Armstrong numbers between {start} and {end} are:")

for i in range(start, end + 1):
    if is_armstrong(i):
        print(i)
print("This code is written and executed by Anjali_0231BCA188")
