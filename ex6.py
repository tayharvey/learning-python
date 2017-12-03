#A variable is created and set equal to 10
types_of_people = 10
#A string is assigned to a variable
x = f"There are {types_of_people} types of people."

#A variable called binary is created
binary = "binary"
#A variable called do_not is created
do_not = "don't"
#A variable called y is created
y = f"Those who know {binary} and those who {do_not}."

#x is printed
print(x)
#y is printed
print(y)

#A string is printed with x
print(f"I said: {x}")
#A string is printed with y
print(f"I also said: '{y}'")

#The variable hilarious is created
hilarious = False
#The variable joke_evaluation is created
joke_evaluation = "Isn't that joke so funny?! {}"

#joke_evaluation is printed with variable hilarious being the response.
print(joke_evaluation.format(hilarious))

#A variable, w, is created
w = "This is the left side of..."
#A variable, e, is created
e = "a string with a right side."

#The variables w and e are printed in that order.
print (w + e)
