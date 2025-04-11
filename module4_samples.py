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
