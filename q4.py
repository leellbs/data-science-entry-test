# def string_reverse(s):
#     """
#     Task 1
#     - Create a function that reverses a given string (s).
#     - s must be a string.
#     - Return the reversed string.
#     """
#    return


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"


def string_reverse(s):
    if isinstance(s, str):
        return s[::-1]


result1 = string_reverse("Hello World")
print("Reversed:", result1)


result2 = string_reverse("Python")
print("Reversed:", result2)
