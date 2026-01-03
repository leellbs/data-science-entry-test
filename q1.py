# def swap(x, y):
#     """
#     Task 1
#     - Create a function that would swap the value of x and y using only x and y as variables.
#     - x and y must be numeric.
#     - Return -1 if x and y is not numeric, and
#     - print the swapped values if both x and y are numeric.
#     """
#     return


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17


def swap(x, y):
#    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
#        return -1
    if not (type(x) in (int, float) and type(y) in (int, float)):
        return -1

    # Swap using arithmetic (no temporary variable)
    x = x + y
    y = x - y
    x = x - y

    return (x,y)

print(swap("Apple", 10))
print(swap(-9, 17))

