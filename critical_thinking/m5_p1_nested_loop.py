# Module 5 - Nested Loop Example
"""This program calculates the total and average monthly
rainfall over one or more years. It starts by asking the
user to input the number of years. Then, for each month
in each year, the program requests the user to enter the
amount of rainfall in inches. Finally, the program calculates
and displays the total inches of rainfall for the entire
period and the average monthly rainfall."""
# Constants
NUM_MONTHS = 12
MONTHS_LIST = [ 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]

# Initialize variables
total_rainfall = 0.0

# Get the number of years from the user
years = int(input("Enter the number of years: "))
while years <= 0:
    print("Invalid input. Please enter a positive number.")
    years = int(input("Enter the number of years: "))

# Loop through each year
for year in range(1, years + 1):
    print(f"\nYear {year}:")
    # Loop through each month
    for month in MONTHS_LIST:
        # Initialize rainfall variable
        rainfall = -1
        # Get the rainfall for the month
        while rainfall < 0:
            try:
                rainfall = float(input(f"Enter the rainfall for {month} (in inches): "))
                if rainfall < 0:
                    print("Invalid input. Please enter a non-negative number.")
            except:
                print("Invalid input. Please enter a non-negative number.")
        # Add to total rainfall
        total_rainfall += rainfall

# Calculate average monthly rainfall
total_months = int(years * NUM_MONTHS)
average_rainfall = total_rainfall / total_months

# Display results
print(f"\nTotal rainfall over {total_months} months: {total_rainfall:.2f} inches")
print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
# End of program