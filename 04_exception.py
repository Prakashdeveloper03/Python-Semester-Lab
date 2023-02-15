# Use a try-except block to handle errors that may occur during the execution of the code
try:
    # Get two numbers from the user, convert them to integers, and store them in the variables `num1` and `num2`
    num1 = int(input("Enter the number 1 : "))
    num2 = int(input("Enter the number 2 : "))

# If the input is not a number (i.e., it cannot be converted to an integer), catch the ValueError exception and handle it
except ValueError:
    print("Non-number value has been given. Please enter numbers only.")

# If no exception is raised, execute the else block
else:
    # Print the sum of the two numbers using f-string formatting
    print(f"{num1} + {num2} = {num1 + num2}")