# this line defines a function called party_guests
def party_guests(guests, dates):
    # this prints a statment with number of guests
    print(f"There are {guests} guests coming!")
    print("Is that everyone?")
    print(f"No, they're bringing {dates} dates!")
    print("Yikes.\n")

print("Passing values directly to function:")
party_guests(20, 15)

print("Using values from script:")
amount_of_guests = 20
amount_of_dates = 37
party_guests(amount_of_guests, amount_of_dates)

print("Doing math inside the function:")
party_guests(34 + 2, 67 +3)

print("Combining variables with math within function:")
party_guests(amount_of_guests + 23, amount_of_dates + 8)

guests = input('How many people are coming? ')
dates = input('How many dates are they bringing? ')
int(guests)
int(dates)
party_guests(guests, dates)
