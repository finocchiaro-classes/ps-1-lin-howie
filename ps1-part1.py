# Ask the user for the first number, store the value in a variable
firstnum = int(input("Enter an integer between 10 and 100: "))

# Ask the user for the second number, store the value in a variable
secondnum = int(input("Enter an integer less than 4: "))

# Repeat back the numbers
print("You entered " + str(firstnum) + " and " + str(secondnum))

# Perform calculations. Be careful about string formatting for autograders.
# Sum
numsum = firstnum + secondnum
print(firstnum, "+", secondnum, "=", numsum)

# Product
numproduct = firstnum * secondnum
print(firstnum, "*", secondnum, "=", numproduct)

# Power (num1^num2)
numpower = firstnum ** secondnum
print(firstnum, "**", secondnum, "=", numpower)

# Remainder
numremainder = firstnum % secondnum
print(firstnum, "%", secondnum, "=", numremainder)






