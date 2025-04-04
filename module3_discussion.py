import array as arr

# Moduel 3 Discussion
# Array example and commom use cases

# An array of students height in centimeters (cm) in a 4th grade classroom
stu_height = arr.array('f', [153.0, 130.6, 140.2, 148.0, 145.7, 155.0, 120.0, 130.3, 131.7, 140.5, 128.6, 127.9, 133.8, 140.0, 149.1])

# Total number of students in the class
num_stu = len(stu_height)

# Total Height of all students in the class
tot_height = 0.0
for h in stu_height:
    tot_height += h

# Mean height of the students
mean_height = tot_height / num_stu

# Height of the tallest student
max_height = max(stu_height)

# Height of the shortest student
min_height = min(stu_height)

# Print all values
print("Total number of students in the class: ", num_stu)
print("Mean height of students in the class in cm: ", f"{mean_height:.1f}")
print("Height of the tallest student in the class: ", f"{max_height:.1f}")
print("Height of the shortest student in the class: ", f"{min_height:.1f}")