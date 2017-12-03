# The variable formatter is created
formatter = "{} {} {} {}"

# Format function replaces four {} with four arguments, then prints these arguments
print(formatter.format(1, 2, 3, 4))
# Format function replaces four {} with four arguments, then prints these arguments
print(formatter.format("one", "two", "three", "four"))
# Format function replaces four {} with four arguments, then prints these arguments
print(formatter.format(True, False, False, True))
# Format function replaces four {} with four arguments, then prints these arguments
print(formatter.format(formatter,formatter,formatter,formatter))
# Format function replaces four {} with four arguments, then prints these arguments
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
