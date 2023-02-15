# Set the variables `file1` and `file2` to the input and output files, respectively
file1, file2 = "files/input.txt", "files/reverse.txt"

# Open the input file (`file1`) for reading and the output file (`file2`) for writing using context managers
with open(file1, "r") as f1, open(file2, "w") as f2:
    # Read the contents of the input file, reverse it, and write it to the output file
    f2.write(f1.read()[::-1])