#the number of cars
cars = 100
#the number of occupants a car can have
space_in_a_car = 4.0
#the number of available drivers
drivers = 30
#the number of passengers
passengers = 90
#cars not used due to carpool system
cars_not_driven = cars - drivers
#number of cars driven
cars_driven = drivers
#number of seats available with carpool system
carpool_capacity = cars_driven * space_in_a_car
#average number of passengers in each car used for carpool
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
