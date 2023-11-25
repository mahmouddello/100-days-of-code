def my_function():
    return 3 * 2
    # return keyword replaces the peace of code with the result of the current calculation


output = my_function()  # By using the return key word, output now equal to 6

print(output)
print('--------')


def format_name(first_name, last_name):
    formated_first_name = first_name.title()
    formated_last_name = last_name.title()
    return f"{formated_first_name} {formated_last_name}"
    # Python String title() method basically converts the input string to title case i.e. it
    # converts only the first character of every word in the input string to Uppercase and
    # converts the rest of the characters to Lowercase.


print(format_name("mahmoud", "dello"))
