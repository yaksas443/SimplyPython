# Source: https://adriann.github.io/programming_problems.html
# Write a program that prints a multiplication table for numbers up to 12

def printTable(number):
	count = 1
	for count in range(1,number+1):
		count2 =1
		print "\n\nTable for " + str(count) + " is \n"
		for count2 in range(1,13):
			print str(count) + " * " + str(count2) + " = " + str(count * count2)
	


num = raw_input ("Please enter a number: ")

printTable(int(num))


