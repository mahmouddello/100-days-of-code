import re

# Count the letters of each word using dictionary comprehensions
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

new_dict = {word: len(word) for word in sentence.strip("?").split()}
print(new_dict)
