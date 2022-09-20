# The most basic form of a data structure is a list
def create_list(args, kwargs):
    """Function for data structure exercise"""

    random_list = list(range(args, kwargs))
    return random_list

# Displaying data structure on console.
describe = create_list(1, 20)
print(describe)