# Create a dictionary `student_marks` with student names as keys and a list of their marks as values
student_marks = {
    'Siva': [85, 76, 92, 88],
    'Akhil': [82, 88, 85, 80],
    'Melvin': [90, 94, 87, 91],
    'Aravind': [78, 82, 80, 75],
    'Krishna': [85, 84, 96, 74, 62]
}

# Print the original dictionary
print(f"Original Dict : {student_marks}")

# Use a dictionary comprehension to create a new dictionary `student_total_marks` with student names as keys and their total marks as values
# The `sum()` function is used to calculate the sum of the marks in each list
student_total_marks = {k : sum(v) for k, v in student_marks.items()}

# Print the updated dictionary
print(f"Updated Dict : {student_total_marks}")

# Use the `max()` function with the `key` argument set to `student_total_marks.get` to find the key (i.e., student name) with the highest value (i.e., total marks)
topper = max(student_total_marks, key=student_total_marks.get)

# Print the name and marks of the student with the highest value in the dictionary
print(f"The topper from the given dict is {topper} with {student_total_marks[topper]} marks")