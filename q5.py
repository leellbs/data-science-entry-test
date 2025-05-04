# def check_divisibility(num, divisor):
#     """
#     Task 1
#     - Create a function to check if the number (num) is divisible by another number (divisor).
#     - Both num and divisor must be numeric.
#     - Return True if num is divisible by divisor, False otherwise.
#     """
#     return


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3


def check_divisibility(num, divisor):
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        print("Both num and divisor must be numeric")
    if divisor == 0:
        print("Divisor cannot be zero")
    return num % divisor == 0


print("10 divisible by 2?", check_divisibility(10, 2))  


print("7 divisible by 3?", check_divisibility(7, 3)) 
