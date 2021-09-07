# this program shows how many passengers can be transported
# by available cars and drivers.

cars = 100  # total available cars
space_in_a_car = 4.0  # the space in one car
drivers = 30  # total available drivers
passengers = 90  # total passengers to transport
cars_not_driven = cars - drivers  # we subtract all cars - available drivers
cars_driven = drivers  # sets new variable for today drivable cars
carpool_capacity = cars_driven * space_in_a_car  # we multiply by cars and their space to get the capacity.
average_passengers_per_car = passengers / cars_driven  # we divide  total passengers by cars driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("there will be", cars_not_driven, "empty cars today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
