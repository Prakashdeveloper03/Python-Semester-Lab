# Define a list of strings
s = ["SIVA", "AKHIL", "PRAKASH", "ARAVIND"]

# Print the original list
print(f"Original list : {s}")

# Convert all strings in the list to lowercase using the `map()` function
# The `map()` function applies the `str.lower()` method to each element of the list `s`
# The `list()` function converts the map object to a list
converted_list = list(map(str.lower, s))

# Print the converted list
print(f"Conversion list : {converted_list}")