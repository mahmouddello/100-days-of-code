def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}\n----------------")
    # BTS: Creating two parameters and taking arguments from the user where we call the function


greet_with("Paris", "Mahmoud")

# Positional Arguments: This is the default way to calling functions in python, because when we call the function,
# we didn't specify anywhere which particular parameter we want to associate the peace of data, so it's just gone to
# the parameter location

greet_with(location="Paris", name="Mahmoud")

# Keyword Arguments: no matter switching the argument places because we use if the keyword arguments nothing going to
# affect the function behavior
