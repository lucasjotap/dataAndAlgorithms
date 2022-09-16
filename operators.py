# The following are some of the operator types Python works with.

# To compare variables we have ==
def comparison(args, kwargs):
    """Comparison function"""
    first = args 
    second = kwargs

    # Using a operator within the funcion to address each variable.
    if first == second:
        print("Variables first and second are a match")
    else:
        print("No match between the numbers.")

comparison(1,1)

# To show a 'greater than' value we have >
def comparisonA(args, kwargs):
    """Show a greater value"""
    first = args
    second = kwargs

    if first > second:
        return "First value is greater."
    elif first == second:
        return "These values are equal."
    else:
        return "Second value is greater."
    
compare_a = comparisonA(1,1)
compare_b = comparisonA(1,2)
compare_c = comparisonA(2,1)
print("\n" + compare_a)
print(compare_b)
print(compare_c)

# To show a 'lesser than' value we have <
def comparisonB(args, kwargs):
    """Show a greater value"""
    first = args
    second = kwargs

    if first < second:
        return "Second value is greater."
    elif first == second:
        return "These values are equal."
    else:
        return "First value is greater."
    
compare_x = comparisonB(1,1)
compare_y= comparisonB(1,2)
compare_z = comparisonB(2,1)
print("\n" + compare_x)
print(compare_y)
print(compare_z)