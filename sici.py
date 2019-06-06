# Source: Understanding Computer Applications with BlueJ - X
# Find difference between Simple Interest and Compound Interest

import math

p = float(raw_input("Enter principle amount (Rs.): "))
r = float(raw_input("\nEnter the rate of interest (%): "))
t = float(raw_input("\nEnter time (years): "))

si = (p*r*t) / 100
amt = p* math.pow((1 + r/100),t)

ci = amt - p
diff = ci - si

print "\nPrinciple : " + str(p) + " Rs"
print "\nRate of interest : " + str(r) + " %"
print "\nTime : " + str(t) + " years"
print "\nCompound Interest : " + str(ci) + " Rs"
print "\nSimple Interest : " + str(si) + " Rs"

print "\nDifference between Compound Interest and Simple Interest is : " + str(diff) + " Rs"
