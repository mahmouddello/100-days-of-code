# let's suppose you want to declare a variable without initilaizing it, but you decided the datatype

age1: int  # now you can assign a value for this variable later on

age1 = 10  # and the type hinting here; prevents us from assigning the wrong datatype value


# We can also use type hinting in functions to escape from errors when we call the function and pass the right parameter
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

# -> arrow means this function is expected to return boolean; either True or False
