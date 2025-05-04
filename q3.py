# def update_dictionary(dct, key, value):
#     """
#     Task 1
#     - Create a function that updates a dictionary (dct) with a new key-value pair.
#     - If the key already exists in dct, print the original value, then update its value.
#     - Return the updated dictionary.
#     """
#     return


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26


def update_dictionary(dct, key, value):
    if key in dct:
        print(f"Original value for '{key}': {dct[key]}")
	# print("Original value for '{}': {}".format(key, dct[key]))
	# print("Original value for '" + str(key) + "': " + str(dct[key]))
    dct[key] = value
    return dct


result1 = update_dictionary({}, "name", "Alice")
print("Updated dictionary:", result1)


result2 = update_dictionary({"age": 25}, "age", 26)
print("Updated dictionary:", result2)
