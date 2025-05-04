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
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1

    # Swap using arithmetic (no temporary variable)
    x = x + y
    y = x - y
    x = x - y

    print("Swapped values: x =", x, ", y =", y)


result1 = swap("Apple", 10)  # Output: No values to swap
print("Result 1:", result1)  # Output: -1 since both x and y are neither int nor float


result2 = swap(-9, 17)       # Output: Swapped values: x = 17 , y = -9
print("Result 2:", result2)  # Output: None (function prints, doesn't return swapped values)
