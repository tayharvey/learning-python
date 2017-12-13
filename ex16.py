# imports argv function
from sys import argv

# assigns variable to argv
script, filename = argv

# prints string with filename
print(f"We're going to erase {filename}.")
# prints first option to avoid deletion
print("If you don't want that, hot CTRL-C (^C).")
# prints second option
print("If you do want that, hit return.")

# prompts user input
input("?")

# prints string
print("Opening the file...")
# assigns variable to open function
target = open(filename, 'w')

# prints string
print("Truncating the file, Goodbye!")
# applies truncate function to file
target.truncate()

# prints string
print("Now I'm going to ask you for three lines.")

# prompts for line1 user input
line1 = input("line 1: ")
# prompts for line2 user input
line2 = input("line 2: ")
# prompts for line3 user input
line3 = input("line 3: ")

# prints string
print("I'm going to write these to the file.")

# writes line1, line2, line3 into file
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

# prints string
print("And finally, we close it.")
# closes file
target.close()
