# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(function(*args))  # we can pass all positional / keyword arguments like this
        return f"You called function: {function.__name__}{args}\n" \
               f"It returned {function(args[0], args[1], args[2])}"

    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(x, y, z):
    return x + y + z


print(a_function(1, 2, 3))
