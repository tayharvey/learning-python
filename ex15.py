# this imports the argv command
from sys import argv
# this uses argv to get a file name
script, filename = argv
# a variable is assigned with the open function
txt = open(filename)
# this prints the string
print(f"Here's your file {filename}:")
# this prints the file
print(txt.read())
# this prints the string
print("Type the filename again:")
# this asks prompts the input
file_again = input("> ")
# this assigns a variable to open the file again
txt_again = open(file_again)
# this prints the variable
print(txt_again.read())
