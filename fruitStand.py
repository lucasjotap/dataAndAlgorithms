choice = input("Hello, welcome to the fruit stand! \n"
"We have bananas(1), apples(2) or oranges(3).\n"
"Select the fruit you wish to purchase:")

produce = [1, 2, 3]

if int(choice) in produce:
    
    amount = int(input("How many? > "))
    # Bananas
    if (choice == 1):
        price = amount * 1.85
    # Apples
    elif (choice == 2):
        price = amount * 2.30
    # Oranges
    else:
        price = amount * 3.60
        
    print("Your order costs %i dollars." % (price))
else:
    # Wrong number selected for item
    print("Product missing.")