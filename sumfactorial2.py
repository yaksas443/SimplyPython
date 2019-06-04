# Source: https://adriann.github.io/programming_problems.html
# Modify the previous program such that only multiples of three or five are considered in the sum, e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
# To convert str to int use int()
# to concatenate int to str, first convert it to str


def divisibleByThree(num):
	if num%3 == 0:
		return True
	else:
		return False

def divisibleByFive(num):
	if num%5 == 0:
		return True
	else:
		return False

def sumFactorial(number):
	count = 0
	sum=0
	for count in range(0,number):
		if number==17:
			if divisibleByFive(count) or divisibleByThree(count):
				sum = sum + count
			else:
				sum = sum + 0
		else:
			sum = sum + count
	return sum


num = raw_input ("Please enter a number: ")

print "Sum: " + str(sumFactorial(int(num)))


