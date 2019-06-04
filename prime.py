# Source: https://adriann.github.io/programming_problems.html
# Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers, printing all primes up to the largest number you can easily represent is fine too.)

def printPrime(number):
	count = 4
	print "\n\nPrime numbers upto " + str(count) + " are \n"
	if number >= 1:
		print "1 \n"
	if number >= 2:
		print "2 \n"
	if number >= 3:
		print "3 \n"	
	for count in range(4,number+1):
		count2 = 2
		flag = 0
		for count2 in range(2,(count/2)+1):
			if count % count2 == 0:
				flag = 1
				break
		if flag == 0:
			print str(count) + "\n"


num = raw_input ("Please enter a number: ")

printPrime(int(num))


