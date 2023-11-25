import random
# Instructions : You are going to write a program which will select a random name from a list of names. The person
# selected will have to pay for everybody's food bill.
######################
# Important: You are not allowed to use the choice() function.
######################
# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to
# work, you must enter all the names as name followed by comma then space. e.g. name, name, name
######################
# Example Input :
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.
#
# Example Output :
# Michael is going to buy the meal today!
# Hint
# You might need the help of the len() function.
# https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list
#
# Remember that Lists start at index 0!
####################################
# Code :
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
random_index = random.randint(0, len(names) - 1)  # indexing starts from 0, so we subtract 1 from the length of the list
print(names[random_index] + " is going to buy the meal today!")
