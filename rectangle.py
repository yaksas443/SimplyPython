# Source: Understanding Computer Applications with BlueJ - X
# Find the area, perimeter and diagonal of a rectangle

import math

l = int(raw_input("Enter the length of rectangle (cm): "))
b = int(raw_input("\nEnter the breadth of rectangle (cm): "))

area = l * b
perimiter = 2 * (l + b)
diagonal	= math.sqrt(l*l + b*b)

print "\nArea of the rectanle is : " + str(area) + " cm^2"
print "\nPerimeter of the rectanle is : " + str(perimiter) + " cm"
print "\nDiagonal of the rectanle is : " + str(diagonal) + " cm"

