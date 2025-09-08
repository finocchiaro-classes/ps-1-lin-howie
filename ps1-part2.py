# Write a function that takes two variables and does all the computations asked
def number_fun(a, b):
    # Repeat back the numbers
    print("You entered " + str(a) + " and " + str(b))

    # Perform calculations.
    # Sum
    numsum = a + b
    print(a, "+", b, "=", numsum)

    # Product
    numproduct = a * b
    print(a, "*", b, "=", numproduct)

    # Power (num1^num2)
    numpower = a ** b
    print(a, "**", b, "=", numpower)

    # Remainder
    numremainder = a % b
    print(a, "%", b, "=", numremainder)
    

# Ask the user for the first number, store the value in a variable
a = int(input("Enter an integer between 10 and 100: "))

# Ask the user for the second number, store the value in a variable
b = int(input("Enter an integer less than 4: "))


# Perform calculations. Be careful about string formatting for autograders.
number_fun(a, b)

