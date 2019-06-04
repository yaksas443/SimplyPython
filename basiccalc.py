# Source: Understanding Computer Applications with BlueJ - X
# Assign two numbers. Find the sum, difference, product and the remainder of two numbers

a = raw_input("Enter number 1: \n")
b = raw_input("Enter number 2: \n")

a = int(a)
b = int(b)

sum = a + b
product = a * b 
remainder = a / b
difference = a - b

print "\nSum: " + str(sum)
print "\nProduct: " + str(product)
print "\nRemainder: " + str(remainder)
print "\nDifference: " + str(difference) 