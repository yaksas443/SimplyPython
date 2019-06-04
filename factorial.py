# Source: https://adriann.github.io/programming_problems.html
# Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1..n.

def printSumFactorial(number):
	count = 0
	sum=0
	for count in range(0,number+1):
		sum = sum + count
	print "Sum factorial for " + str(number) + " is " +  str(sum)

def printNormalFactorial(number):
	count = 0
	sum=1
	for count in range(1,number+1):
		sum = sum * count
	print "Normal factorial for " + str(number) + " is " +  str(sum)


num = raw_input ("Please enter a number: ")
choice = raw_input("\n1. Sum factorial\n2. Normal Factorial\nEnter a number (1,2): ")

if choice=='1':
	printSumFactorial(int(num))
elif choice=='2':
	printNormalFactorial(int(num))



