# Writing the first version in compound algorithms 

# Write a script that accepts two integers and compares which is greatest
# If the first given value happens to be the greater one, a message should be printed say so.

# x = input("Insert an integer here: ")
# y = input("Insert the second integer: ")

# if (x > y):
#     print("The first value is the the greater one.\n" + f"Value: {x}" )
# else: 
#     print("The second value is the the greater one.\n" + f"Value: {y}" )

# Second version 
def compare():
    """Compare two values and return a msg depending on the result."""
    x = int(input("Enter an integer here: "))
    y = int(input("Enter another integer here: "))

    if (x>y):
        print("The first digit is greater.\n" + "Value %i" % (x))
    else:
        print("The second digit is greater.\n" + "Value %i" % (y))

compare()