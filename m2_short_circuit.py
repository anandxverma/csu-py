# Short-circuit Example 1:
# In this case, the evaluation stops at (3 > 4) because it renders the whole condition false
# Therefore the Else statement is executed
if (3 > 4) and (6 > 5):
	print("This is hilarious.")
else:
	print("I am not having fun.")


# Short-circuit Example 2:
# In this case, the conditions (3 > 4) is evaluated first, followed by (6 > 5) and stops
# Because it renders the whole condition True
# Therefore the If statement is executed
if (3 > 4) or (6 > 5) or (7 > 8):
	print("This is hilarious.")
else:
	print("I am not having fun.")
