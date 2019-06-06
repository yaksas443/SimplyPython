# Source: Understanding Computer Applications with BlueJ - X
# PCB Marks

p = int(raw_input("Enter marks in Physics : "))
c = int(raw_input("Enter marks in Chemistry : "))
b = int(raw_input("Enter marks in Biology : "))

total = p + c + b
average = total / 3

print "\nTotal marks: " + str(total)
print "\nAverage marks: " + str(average)