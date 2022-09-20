def bonus():
    """Define a model for an yearly company bonus"""
    hire_date = int(input("What year were you hire in? > "))
    current_yr = int(input("What year is this? > "))

    # Getting the amount if time one's worked for the company
    time_amount =  current_yr - hire_date

    if (time_amount >= 5):
        # If the person's amount of time in the company >=5 give 20% bonus over salary.
        salary = int(input("Salary amount: "))
        salary_bonus = salary * 0.2
        salary += salary_bonus

    else:
        # If the person's amount of time in the company < 5 give 10% bonus over salary.
        salary = int(input("Salary amount: "))
        salary_bonus = salary * 0.1
        salary += salary_bonus
    
    print("Total amount for your salary this month: %i.\n" %(salary_bonus) +  
    "Your salary amount: %i ." %(salary))

bonus()