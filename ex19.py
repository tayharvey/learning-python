# this line defines a function called cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # line of the function that prints the number of cheeses
    print(f"You have {cheese_count} cheeses!")
    # line that prints number of boxes of crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # line that prints statement
    print("Man that's enough for a party!")
    # line that prints statement (neither of these lines changes according to input values)
    print("Get a blanket.\n")

# prints statement
print("We can just give the function numbers directly:")
# calls the above function and inserts numbers directly
cheese_and_crackers(20,30)

# prints statement
print("OR, we can use variables from our script:")
# assigns value to variables in script
amount_of_cheese = 10
# assigns value to variables in script
amount_of_crackers = 50

# calls function with assigned variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints statement
print("we can even do math inside too:")
# performs math within function to obtain result
cheese_and_crackers(10 + 20, 5 +6)

# prints statement
print("and we can combine the two, variables and math:")
# performs math combined with variables to obtain result
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
