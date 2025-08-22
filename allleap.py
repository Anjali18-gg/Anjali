def is_leap_year(year):
    if(year%4 == 0 and year%100!=0) or (year%400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year:"))
if is_leap_year(year):
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")
count = 0
for i in range(1,2025,1):
    if is_leap_year(i):
        print(f"Year: {i}")
        count+=1
print(f"total count:{count}")
print("This code is written and executed by Anjali_0231bca188")
