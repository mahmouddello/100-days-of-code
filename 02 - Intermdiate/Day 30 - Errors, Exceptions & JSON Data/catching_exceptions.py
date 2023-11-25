# The try catch except finally Pattern


try:
    file = open("some_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])  # if u want to see error enter a random key name
    # try comes for a block of code where you're trying to execute that might cause an exception,
    # in most cases it probably will work, but sometimes it just might not.
except FileNotFoundError:
    file = open("some_file.txt", mode="w")
    file.write("Something")
    # This is the block of code that you want the computer to execute if there were an exception.
    # If something went wrong, carry ou this piece of code. (Do this if there was an exception)
    # Note: There are too many error exceptions, and we can write more than one exception.
except KeyError as error:
    print(f"The Key {error} doesn't exist!")  # This exception is for the dictionary KeyError!
else:
    content = file.read()
    print(content)
    # This block allows you to define some code to execute if there was no exception

finally:
    file.close()
    print(f"file is closed.")
    # Execute this piece of code no matter what happens

# Raising your own exception with raise Keyword:

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
