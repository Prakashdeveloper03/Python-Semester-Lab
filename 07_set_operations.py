# Create a set of squares of the numbers 1 to 10 using a set comprehension
s = {x ** 2 for x in range(1, 11)}

# Add elements to the set using the `add()` method
s.add(11)
s.add(12)

# Print the updated set
print(f"After add() : {s}")

# Remove elements from the set using the `remove()` method
s.remove(11)
s.remove(12)

# Print the updated set
print(f"After remove() : {s}")

# Pop elements from the set using the `pop()` method
s.pop()
s.pop()

# Print the updated set
print(f"After pop() : {s}")

# Add multiple elements to the set using the `update()` method
s.update([11, 12])

# Print the updated set
print(f"After update() : {s}")

# Clear the set using the `clear()` method
s.clear()

# Print the updated set
print(f"After clear() : {s}")