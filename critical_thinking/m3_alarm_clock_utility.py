import re
import datetime as dt
import array as arr

# This program defines utility functions for the alarm clock program

def __get_hr_min(time_str):
    hours, minutes = 0, 0
    if ":" in time_str:
        hours, minutes = map(int, time_str.split(":"))
    else:
        hours = int(time_str)
        minutes = 0

    return arr.array("i", [hours, minutes])

# Validate if the provided time is in hh:mm 24 hrs format
# Any of the following formats are accepted:
# hh:mm (example: 23:59)
# h:mm (example: 1:05)
# hh (example: 14)
# h (example: 18)
def validate_24hr_format(time_str):
    # The following regex pattern matches the hh:mm or h:mm format
    pattern1 = r"^([01]?[0-9]|2[0-3]):[0-5][0-9]$"
    # The following regex pattern matches the hh or h format
    pattern2 = r"^([01]?[0-9]|2[0-3])$"
    
    # Check if the current time matches either of the patterns
    match = re.match(pattern1, time_str) or re.match(pattern2, time_str)
    
    # If the time_str is in the correct format, then return the hours and minutes
    # Otherwise, return False
    if match:
        return __get_hr_min(time_str)
    else:
        return False

# Validate if the provided time is in hh:mm
# Any of the following formats are accepted:
# hh:mm (example: 56:59)
# h:mm (example: 33:05)
# hh (example: 14)
# h (example: 26)
def validate_hr_min_format(time_str):
    # The following regex pattern matches the hh:mm or h:mm format
    pattern1 = r"^(\d+:[0-5][0-9])$"
    # The following regex pattern matches the hh or h format
    pattern2 = r"^(\d+)$"
    
    # Check if the current time matches either of the patterns
    match = re.match(pattern1, time_str) or re.match(pattern2, time_str)
    
    # If the time_str is in the correct format, then return the hours and minutes
    # Otherwise, return False
    if match:
        return __get_hr_min(time_str)
    else:
        return False
