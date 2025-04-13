for i in range(3):
    print(i)
print("Last iterator count:", i)
print()

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
print('Current Letter :', letter)
print()

fruits = ["apple", "orange", "kiwi"]
iter_obj = iter(fruits)
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break

#FIXME
# The code below is not working as expected
print()
clist = ['Canada','USA','Mexico','Australia']
for i in clist:
    print(i)

list1 = ["A", "B", "C"]
print("C" in list1)
print("D" in list1)

print()
stu_grades = [ 3.7, 3.3, 2.7, 1.9, 3.8, 4.0, 4.0, 3.9, 3.6, 2.9, 2.1, 2.3, 2.2, 4.0, 3.8, 3.3, 3.1, 3.1, 3.3, 2.4, 2.7, 2.3, 1.9, 1.7, 3.6, 3.9, 4.0, 4.0 ]

grp_high = []
grp_med = []
grp_low = []

for i in range(len(stu_grades)):
    grade = stu_grades[i]
    if grade >= 3.5:
        grp_high.append(grade)
    elif grade < 3.5 and grade >= 2.0:
        grp_med.append(grade)
    else:
        grp_low.append(grade)

print(grp_high)
print(grp_med)
print(grp_low)