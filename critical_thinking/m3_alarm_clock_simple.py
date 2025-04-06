import re
import datetime as dt

# This program calculates when the alarm will go off
# based on the current hr as provided by the user and
# the number of hrs to set the future alarm

# Ask the user to input the current time in 24hr or accept the current time
current_time_in_hrs = input("Enter the current time in 24hr format or hit ENTER to accept the current time: ") or str(dt.datetime.now().hour)

# Check the current time if it matches the 24hr format
# Any of the following formats are accepted:
# hh (example: 14)
# h (example: 5)
# The following regex pattern matches the hh or h format
pattern = r"^([01]?[0-9]|2[0-3])$"
# Check if the current time matches either of the patterns
match = re.match(pattern, current_time_in_hrs)
# Exit program if the input is not in the correct format
if not match:
    print("Invalid time format. Please enter the time in 24hr format without the trailing minutes. Example: 14")
    exit()

# Ask the user to input the number of hrs to set the future alarm
hrs_to_wait_for_alarm = int(input("Enter the number of hrs to wait for the alarm: "))
# Check for valid input
if hrs_to_wait_for_alarm < 0:
    print("Invalid input. Please enter a valid value for number of hrs.")
    exit()

# Calculate the future alarm time
total_hrs_to_wait = int(current_time_in_hrs) + hrs_to_wait_for_alarm
# Calculate the number of days and hrs to wait for the alarm
num_days_to_wait = total_hrs_to_wait // 24
num_hrs_to_wait = total_hrs_to_wait % 24

print("*" * 60)
# Print the results
if num_days_to_wait == 0:
    print("     The alarm is set to go off today at", num_hrs_to_wait, "o'clock.")
elif num_days_to_wait == 1:
    print("     The alarm is set to go off tomorrow at", num_hrs_to_wait, "o'clock.")
else:
    print("     The alarm is set to go off in", num_days_to_wait, "days at", num_hrs_to_wait, "o'clock.")
print("*" * 60)