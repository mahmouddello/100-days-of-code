# Functions that allows inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name} ?")
    print(f"Isn't the weather good today {name} ?\n-----------------")
    # Behind the scenes we are creating a variable called (name) and we are passing a parameter throw function
    # so our parameter will be assigned to the name variable


greet_with_name("Mahmoud")  # When we call the function we are passing a peace of data

# The passed string here called : Argument "Mahmoud"
# Parameter : name, which is getting data from the function
