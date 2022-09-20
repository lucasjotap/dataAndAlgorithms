# Logic in Python
# Considering the following three values.
x = 10
y = 5.5
z = 9

# The result will be false since the operator AND requires both premises to be true. 
print(x > y and z == x)
# The result here is true since both premises are true.
print(x > y and z < x)

# Using the or operator you can get different results as well.
# The output here is true because only one premise needs to be true.
print("\n" + str(y > x or z < x))
# The output here is false because at least one premise needs to be true.
print(y > x or x < z)