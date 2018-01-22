# this imports argv
from sys import argv

#this
script, input_file = argv

# this defines the function print_all with argument f
def print_all(f):
    # this prints the results of reading a file
    print(f.read())

# this defines the rewind function with arguent f
def rewind(f):
    # this uses the seek function within the file
    f.seek(0)

# this defines the print_a_line function with arguments line_count and f
def print_a_line(line_count, f):
    # this prints the line number and the line itself
    print(line_count, f.readline())

# this assigns the variable current_file to a user input
current_file = open(input_file)

# this prints a string
print("First let's print the whole file:\n")

# this prints the entire file that was called
print_all(current_file)

# this prints a string
print("Now let's rewind, kind of like a tape.")

# this calls the rewind function with variable current_file
rewind(current_file)

# this prints a string
print("Let's print three lines:")

# this assigns a line number
current_line = 1
# this prints the above line number with text of that line
print_a_line(current_line, current_file)

# this assigns a line number
current_line = current_line + 1
# this prints the above line number with text of that line
print_a_line(current_line, current_file)

# this assigns a line number
current_line = current_line + 1
# this prints that number with the text of that line
print_a_line(current_line, current_file)
