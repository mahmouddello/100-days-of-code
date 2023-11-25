# Dictionary. Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is
# ordered*, changeable and do not allow duplicates

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again"
}

# Bug, Function and Loop here are the keys.
# After every key there is a colon and then there is the value of that key

print(programming_dictionary["Bug"])  # inside the square brackets we pass our key and be careful with typing errors
print("---------------------------------")
# Adding new items to dictionary
programming_dictionary["List"] = "Lists are used to store multiple items in a single variable"
programming_dictionary[1] = 6
print(programming_dictionary)
print("---------------------------------")

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary

# programming_dictionary = {}

# print(programming_dictionary)

# Edit an item in dictionary

programming_dictionary["Bug"] = "a moth in your computer"

print(programming_dictionary)
print("-----------------------------------")
# Loop through a dictionary

for thing in programming_dictionary:
    print(thing)
    # this code just gives you the keys.
print("-----------------------------------")
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    # this code will print the keys and values
