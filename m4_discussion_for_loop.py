# "for" Loop Example 1
# This example demonstrates thr for loop by using elements counter
# Syntax for <i> in range(0, n)
# In this example, we will catagorize stduent grades into
# high (3.5 or above), medium (2 to 3.5), and low (below 2)

# Define the list of student grades
grades = [ 3.7, 3.3, 2.7, 1.9, 3.8, 4.0, 4.0, 3.9, 3.6, 2.9, 2.1, 2.3, 2.2, 4.0, 3.8, 3.3, 3.1, 3.1, 3.3, 2.4, 2.7, 2.3, 1.9, 1.7, 3.6, 3.9, 4.0, 4.0 ]

# Initialize the grade groups
high_grades = []
medium_grades = []
low_grades = []

# Find the number of students
num_students = len(grades)

# Arrange the grades into groups
for i in range(0, num_students):
    if grades[i] >= 3.5:
        high_grades.append(grades[i])
    elif grades[i] >= 2:
        medium_grades.append(grades[i])
    else:
        low_grades.append(grades[i])

# Print the results
print("\"for\" loop example 1: for <i> in range(0, n)")
print("High Grades:", high_grades)
print("Medium Grades:", medium_grades)
print("Low Grades:", low_grades)
print()

# "for" Loop Example 2
# This example demonstrates a variation of the for loop
# by iterating over the elements of a list
# Syntax: for e in list
# Re-initialize the grade groups
high_grades.clear()
medium_grades.clear()
low_grades.clear()
# Arrange the grades into groups
for g in grades:
    if g >= 3.5:
        high_grades.append(g)
    elif g >= 2:
        medium_grades.append(g)
    else:
        low_grades.append(g)

# Print the results
print("\"for\" loop example 2: for <e> in <list>")
print("High Grades:", high_grades)
print("Medium Grades:", medium_grades)
print("Low Grades:", low_grades)
print()

# "for" Loop Example 3
# This example demonstrates loop compression technique in Python
# Loop compression makes the code more compact, readable, and efficent
# Syntax: [ <do something on the item> for <item> in <list> ]
# The example also demonstrates the use of Ternary operator
# Syntax: <value1> if <condition is true> else <value2>
# Re-initialize the grade groups
# Re-initialize the grade groups
high_grades.clear()
medium_grades.clear()
low_grades.clear()
[high_grades.append(g) if g >= 3.5 else medium_grades.append(g) if g >= 2 else low_grades.append(g) for g in grades]

# Print the results
print("\"for\" loop compression example 3")
print("High Grades:", high_grades)
print("Medium Grades:", medium_grades)
print("Low Grades:", low_grades)