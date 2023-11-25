import time


# Decorator: A Function that has a wrapper function, which adds more functionality to another function,
# for example in the code below we want a delay for 2 seconds in each function,
# we can do it by typing time.sleep(2) in each function, or we can use decorator '@'
# decorator adds this functionality to each function calls it without typing boilerplate code over and over

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after

    return wrapper_function


@delay_decorator  # delays for 2 sec
def say_hello():
    print("Hello")


# With the @ syntactic sugar
@delay_decorator  # delays for 2 sec
def say_bye():
    print("Bye")


# Without the @ syntactic sugar
def say_greeting():
    print("How are you?")


decorated_function = delay_decorator(say_greeting)
decorated_function()
