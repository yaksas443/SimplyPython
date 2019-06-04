# Source: https://adriann.github.io/programming_problems.html
# Modify the previous program such that only the users Alice and Bob are greeted with their names.
# In Python 2 use raw_input(). In Python 3 use input()
name = raw_input ("Please enter your name: ")

if name=="Alice" or name=="Bob":
	print "\nHello, " + str(name)