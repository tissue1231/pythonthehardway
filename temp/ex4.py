#cars
cars = 100
#space
space_in_a_car = 4
#drivers
drivers = 30
#passengers
passengers = 90
#cars not driven
cars_not_driven = cars - drivers
#cars driven
cars_driven = drivers
#carpool
carpool_capacity = cars_driven * space_in_a_car
#average
average_passengers_per_car = passengers / cars_driven


print "there are", cars, "cars available."
print "there are only", drivers, "drivers available."
print "there will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "in each car"