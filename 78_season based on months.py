# Program to determine season based on month

# Take month input from user
month = input("Enter the month name: ").strip().lower()

# Determine season
if month in ("december", "january", "february"):
    season = "Winter"
elif month in ("march", "april", "may"):
    season = "Spring"
elif month in ("june", "july", "august"):
    season = "Summer"
elif month in ("september", "october", "november"):
    season = "Autumn"
else:
    season = "Invalid month name!"

# Display result
print(f"The season in {month.capitalize()} is {season}.")
print("This code is written and executed by Anjali_0231BCA188")
