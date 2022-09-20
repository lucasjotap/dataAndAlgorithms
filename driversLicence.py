# Develop an alorithm that requests your birthday and the current year
# Display the age result on the console

def person():
    """Define a person's age"""
    # Requesting input
    birthday_date = int(input("Insert the year you were born in: "))
    current_date = int(input("Insert the current year you are in: "))

    person_age = current_date - birthday_date

    if (person_age > 18):
        print("You are %i years-old and can get a driver's license if you wish." % (person_age))
    else:
        print("Your age is %i. You can't get a driver's license yet." % (person_age))

person()