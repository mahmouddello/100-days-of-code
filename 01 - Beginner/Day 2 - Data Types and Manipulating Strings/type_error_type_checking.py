num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters.") : this code not going to work because you can only concatenate
# string data types together . concatenate = تجميع
# We can use the type() function to determine what is our variables' data type
type(num_char)
print("Your name has " + str(num_char) + " characters.")  # So here we should convert our integer data type variable
# into a string data type we need to use the str() function.
print(100.5 + float("70"))  # Type casting the string "70" to a float >> 70.0
print(str(150) + str(70))  # Type casting both of integers to a string and concatenate them into a single string


# Summary :
# You can use the 'type()' function to investigate the data type you working with
# Use methods like : str() - int() - float() to convert to that data type

