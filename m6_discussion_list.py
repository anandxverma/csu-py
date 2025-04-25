import time
import random

""" This program simulates a weekly temperature forecast.
    It starts with a predefined forecast of weekly temperatures
    and updates it daily by removing the first temperature from the list
    and adding a new temperature at the end of the list.
"""

# Method to simulate new temperature data
def get_new_temperature():
    # Simulate getting a new temperature value
    return random.randint(50, 100)

# Method to print the weekly temperature forecast
def print_forecast(forecast):
    print("Weekly temperature forecast:")
    print(forecast)
    print()

# Set initial weekly temperature forecast
weekly_temp = [ 56, 59, 60, 60, 72, 79, 81 ]

# Print the current forecast
print("Current forecast")
print_forecast(weekly_temp)

# Simulate moving to the next day for 3 consecutive days
for i in range(3):
    print("Moving to the next day...")
    time.sleep(5)
    # Update the forecast
    weekly_temp.pop(0)
    weekly_temp.append(get_new_temperature())
    # Print the updated forecast
    print_forecast(weekly_temp)
