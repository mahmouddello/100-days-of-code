import random

random_integer = random.randint(1, 10)  # returns a random integer number between 1 and 10
# specifying the beginning and the end rage between the parentheses
print("Random integer between specified range: " + str(random_integer))

random_float = random.random()  # returns a random float in range of [0, 1)
print("Before Multiplying: " + str(random_float))
# if we want to range manually, we can multiply the random to the range without making it indeed
# Example: random_float could be as a maximum 0.999999, so if we multiply it by 5 the range will be [0, 5)
random_float *= 5
print("After Multiplying: " + str(random_float))
random_float_range = random.uniform(10, 15)  # Returns a random float number between a range

print("Random float with specified range: " + str(random_float_range))

random_float_rounded = round(random.uniform(33.33, 66.66), 2)  # Returns a random float number up to 2 decimal places

print("Random float with specified range and then rounded to two decimal: " + str(random_float_rounded))
