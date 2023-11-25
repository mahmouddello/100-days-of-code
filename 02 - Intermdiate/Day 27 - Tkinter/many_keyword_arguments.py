# **kwargs = Many keyword arguments, unlimited keyword arguments

def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    # Dictionary
    for key, value in kwargs.items():
        pass
    n += kwargs.get("add")
    n *= kwargs.get("multiply")
    # get method replaces the kwargs["add"], returns None if the parameter doesn't initialized


calculate(2, add=3, multiply=6)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        # get method returns None if the parameter didn't specify by the user


myCar = Car(make="Nissan", model="GT-R")
print(myCar.model)
print(myCar.color)  # returns None
