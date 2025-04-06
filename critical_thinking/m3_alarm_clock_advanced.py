import re
import datetime as dt
import m3_alarm_clock_utility as m3utl

# This program calculates when the alarm will go off in the future
# based on the current time provided by the user and
# the number of hrs and minutes to set the future alarm

# Ask the user to input the current time in 24hr format or accept the current time
curr_clock_time = str(dt.datetime.now().strftime("%H:%M"))
curr_time = input("Enter the current time in 24hr format as hh:mm or hit ENTER to accept the current time " + curr_clock_time + " o'clock: ") or curr_clock_time

# Check the current time if it matches the 24hr format
# If it matches, then get the hours and minutes
curr_hr_min = m3utl.validate_24hr_format(curr_time)

# Exit program if the input is not in the correct format
if not curr_hr_min:
    # Print an error message and exit the program
    print("Invalid time format. Please enter the time in 24hr format.")
    exit()

# Ask the user to input the number of hrs to set the future alarm
time_to_alarm = input("Enter the hrs and min as hh:mm to set the alarm: ")

# Check the user input if it matches the hh:mm format
# If it matches, then get the hours and minutes
hrs_min_to_alarm = m3utl.validate_hr_min_format(time_to_alarm)

# Check for valid input
if not hrs_min_to_alarm:
    print("Invalid input. Please enter the value in the hh:mm format")
    exit()

# Calculate the future alarm time
# Convert all times into minutes
curr_time_in_min = curr_hr_min[0] * 60 + curr_hr_min[1]
time_to_alarm_in_min = curr_hr_min[0] * 60 + curr_hr_min[1]
min_to_alarm = hrs_min_to_alarm[0] * 60 + hrs_min_to_alarm[1]
# Calculate the total minutes to set the future alarm
tot_min_to_alarm = curr_time_in_min + min_to_alarm
# Calculate the number of days and hrs to wait for the alarm
days_to_alarm = tot_min_to_alarm // 1440 # 1Day = 24hrs * 60min
hrs_to_alarm = (tot_min_to_alarm % 1440) // 60
min_to_alarm = (tot_min_to_alarm % 1440) % 60

# Print the results
print("*" * 63)
display_alarm_time = dt.datetime.strptime(str(hrs_to_alarm) + ":" + str(min_to_alarm), "%H:%M").strftime("%H:%M") + " o'clock."
if days_to_alarm == 0:
    print("    The alarm is set to go off today at", display_alarm_time)
elif days_to_alarm == 1:
    print("    The alarm is set to go off tomorrow at", display_alarm_time)
else:
    print("    The alarm is set to go off in", str(days_to_alarm), "days at", display_alarm_time)
print("*" * 63)
