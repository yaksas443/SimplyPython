# Source: https://adriann.github.io/programming_problems.html
# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
# To convert str to int use int()
# to concatenate int to str, first convert it to str

def sumFactorial(number):
	count = 0
	sum=0
	for count in range(0,number):
		sum = sum + count
	return sum


num = raw_input ("Please enter a number: ")

print "Sum: " + str(sumFactorial(int(num)))


