# Develop an algorithm that asks the user for two integers. 
# Print the sum of both integers on the screen.

# First introduce the practice and request numbers from user

def summing(args, kwargs):
    print("Welcome to the first problem, we'll request two integers from you.")

    # Setting up functions's attibutes
    args = int(input("Please select any integer for this exercise: "))
    kwargs = int(input("Another integer of you choice: "))
    print ("These were the integers you've chosen: %i and %i" % (args, kwargs))
    phrase = f"When you add these values you get: {args + kwargs}"
    return phrase

# Calling funtion in
x = summing(1, 2)
print(x)