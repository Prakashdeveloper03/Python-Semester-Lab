# Generate a list of the first 20 odd numbers using a list comprehension
# The range starts from 1 and goes up to (but not including) 40
# The `if` condition filters out even numbers using the modulo operator (%)
# The resulting list of odd numbers is stored in a list and formatted as a string using an f-string
print(f"First 20 odd numbers : {[x for x in range(1, 40) if x % 2 != 0]}")