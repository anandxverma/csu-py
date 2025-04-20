import array as arr

# Module 5 - Award Points System - Option 3
# This program calculates the award points earned
# by determining the number of books purchased within
# a range according to the points table shown below
# This imlementation is same as Option 2 except for
# it uses dictionary
"""This program calculates the award points earned
by a book club member in a month based on the number
of books purchased, according to the following points table:
----------------------------------------
No. of Books Purchased    Points Earned
----------------------------------------
0 to 1                                0
2 to 3                                5
4 to 5                               15
6 to 7                               30
8 or more                            60
----------------------------------------
The program asks the user to enter the number of books
purchased in the current month and displays the points awarded.
"""
# Book award points table
# Array index represents the number of books purchased
# And the corresponding value represents the points earned
points_table = arr.array('i', [0, 0, 5, 5, 15, 15, 30, 30, 60])

# Initialize variables
books_purchased = -1
# Get the number of books purchased from the user
while books_purchased < 0:
    books_purchased = int(input("Enter the number of books purchased this month: "))
    if books_purchased < 0:
        # Validate the input
        print("Invalid input. Please enter a non-negative number.")

# Determine the points earned based on the number of books purchased
# Use the points_table array to get the points earned
# The index of the array is the number of books purchased
# If the number of books purchased is greater than the length of the array,
# use the last value in the array
if books_purchased >= len(points_table):
    points_earned = points_table[-1]
else:
    points_earned = points_table[books_purchased]

# Display the points earned
print(f"Points earned this month: {points_earned}")