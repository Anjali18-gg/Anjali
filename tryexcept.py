try:
    number = int(input("Enter a number:"))
    result = 10/number
except ZeroDivisionError:
    print("Error:cannot divide by zero.")
except ValueError:
    print("Error:Invalid input.Please enter a valid number.")
print("This code is written and executed by Anjali_0231BCA188")                                
