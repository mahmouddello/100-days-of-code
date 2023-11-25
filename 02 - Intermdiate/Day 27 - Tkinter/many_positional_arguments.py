# *args : Many Positional Arguments

# Unlimited positional arguments function
def add(*args):
    sum = 0
    print(type(args))  # tuple
    for n in args:
        sum += n
    return sum


print(add(3, 5, 7, 8, 12, 10, 123, 214, 901))
