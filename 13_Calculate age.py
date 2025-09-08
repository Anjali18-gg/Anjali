from datetime import datetime

# Input birthdate
birth_date = input("Enter your birth date (dd-mm-yyyy): ")
birth_date = datetime.strptime(birth_date, "%d-%m-%Y")

# Input given date
given_date = input("Enter the given date (dd-mm-yyyy): ")
given_date = datetime.strptime(given_date, "%d-%m-%Y")

# Calculate age
age = given_date.year - birth_date.year

# Adjust if birthday not reached yet in given year
if (given_date.month, given_date.day) < (birth_date.month, birth_date.day):
    age -= 1

print(f"\nYour age on {given_date.strftime('%d-%m-%Y')} is: {age} years")
print("This code is written and executed by Anjali_0231BCA188")
