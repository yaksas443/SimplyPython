# Source: Understanding Computer Applications with BlueJ - X
# Accept number of days and display the result after converting it into number of years, number of months and the remaining number of days

days = int(raw_input("Enter number of days : "))

years = days / 365

rem = days % 365

months = rem / 30

rem = rem % 30

print "\nYears: " + str(years)
print "\nMonths: " + str(months)
print "\nDays: " + str(rem)