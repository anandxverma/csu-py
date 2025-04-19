# Module 5 - Award Points System - Option 1
# This program calculates the award points earned
# by matching the exact number of books purchased
# according to the points table shown below
"""This program calculates the award points earned
by a book club member in a month based on the number
of books purchased, according to the following points table:
----------------------------------------
No. of Books Purchased    Points Earned
----------------------------------------
0                                     0
2                                     5
4                                    15
6                                    30
8 or more                            60
----------------------------------------
The program asks the user to enter the number of books
purchased in the current month and displays the points awarded.
"""
# Constants
POINTS_FOR_0_BOOKS = 0
POINTS_FOR_2_BOOKS = 5
POINTS_FOR_4_BOOKS = 15
POINTS_FOR_6_BOOKS = 30
POINTS_FOR_8_OR_MORE_BOOKS = 60
# Initialize variables
books_purchased = -1
# Get the number of books purchased from the user
while books_purchased < 0:
    books_purchased = int(input("Enter the number of books purchased this month: "))
    if books_purchased < 0:
        # Validate the input
        print("Invalid input. Please enter a non-negative number.")
# Determine the points earned based on the number of books purchased
if books_purchased == 0:
    points_earned = POINTS_FOR_0_BOOKS
elif books_purchased == 2:
    points_earned = POINTS_FOR_2_BOOKS
elif books_purchased == 4:
    points_earned = POINTS_FOR_4_BOOKS
elif books_purchased == 6:
    points_earned = POINTS_FOR_6_BOOKS
elif books_purchased >= 8:
    points_earned = POINTS_FOR_8_OR_MORE_BOOKS
else:
    points_earned = 0

# Display the points earned
print(f"Points earned this month: {points_earned}")