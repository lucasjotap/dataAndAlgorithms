# bonus 20% for ppl who are working 5 years +
# everyone else gets 10% only.


def bonus():
    """Define a bonus model for employees"""

    year_in_company = input("Have you been working here for five years or more? > Y or N: ")
    
    if (year_in_company == "y".lower()):

        salary = int(input("Insert your salary here: "))
        bonus = salary / 5

        print(f"Your bonus this year will be {bonus} dollars.")
    
    else: 
        salary = int(input("Insert your salary here: "))
        bonus = salary / 10

        print(f"Your bonus this year will be {bonus} dollars.")
        
bonus()