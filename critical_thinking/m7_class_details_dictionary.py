"""The program lets a user enter a course number and displays 
the course's room number, instructor, and meeting time. 
It looks up the relevant course details from three dictionary objects, 
each using the course numbers as the keys. One dictionary stores 
the room numbers, the second stores the instructor names, and 
the third stores the meeting times by the course numbers."""

# Create a dictionary of course numbers and room numbers
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

# Create a dictionary of course numbers and instructor names
instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# Create a dictionary of course numbers and meeting times
meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Get the course number from the user
course_number = input("\nEnter a course number (e.g., CSC101): ").upper()
# Check if the course number is valid
if course_number in room_numbers:
    # Display the course details
    print("\nHere are your course details")
    print("-" * 30)
    print("Room Number:", room_numbers[course_number])
    print("Instructor:", instructors[course_number])
    print("Meeting Time:", meeting_times[course_number])
    print()
else:
    # Display an error message if the course number is not found
    print("\nError: Course not found, please check the course number and try again.\n")
# End of program
