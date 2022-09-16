# Develop an algorithm that asks the user for two integers. 
# Print the sum of both integers on the screen.

# First introduce the practice and request numbers from user

def summing(args, kwargs):
    print("Welcome to the first problem, we'll request two integers from you.")

    args = int(input("Please select any integer for this exercise: "))
    kwargs = int(input("Another integer of you choice: "))
    return args + kwargs

x = summing(1, 2)

print(x)