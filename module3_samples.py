import numpy as np
import array as arr

# Complex Number Type
c1 = complex(3, 4)
print(c1)

# Tuples split example
(age, income) = "32,10000".split(",")
print(age)
print(income)

# Array slicing
list1 = [1, 7, 4, 3, 8, 9, 11]
array1 = arr.array('i', list1)
print(array1)
print(array1[2:5])

# Simple statistical computations
class_height = arr.array('f', [130.6, 140.2, 110.0, 112.3, 105.7, 110.3, 105.5])
print(min(class_height))
print(f"{max(class_height):.1f}")

num_students = len(class_height)
total_height = 0
for i in class_height:
    total_height += i
mean_height = total_height / num_students
print(f"{mean_height:.1f}")
