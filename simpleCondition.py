# Sequential algorithms

# Sequence of steps based on certain decision structures.

# Write a script that accepts two integers and compares which is greatest
# If the first given value happens to be the greater one, a message should be printed say so.

#Writinng the first version in simple algorithm
# x = input("Insert an integer here: ")
# y = input("Insert the second integer: ")
# if (x > y):
#    print("The first value is the the greater one.\n" + f"Value: {x}" )

# Second version 
def compare():

    x = int(input("Insert first number here: "))
    y = int(input("Insert ssecond number here: "))
    msg = "The first number is the greater one. \n" + "Value: %i" %(x)

    if (x > y):
        print(msg)

compare()
compare()