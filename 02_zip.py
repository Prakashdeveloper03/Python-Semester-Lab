# Create two lists, one containing arithmetic expressions as strings, and the other containing their corresponding results
expr_list = ["1 + 5", "5 + 8", "12 + 5"]
result_list = ["6", "13", "17"]

# Use the `zip()` function to combine the two lists into a list of tuples, with each tuple containing an expression and its result
# Then, use the `dict()` function to convert the list of tuples into a dictionary, with each expression as the key and its result as the value
result_dict = dict(zip(expr_list, result_list))

# Print the resulting dictionary
print(result_dict)