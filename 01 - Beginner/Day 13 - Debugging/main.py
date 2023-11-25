from random import randint


############DEBUGGING#####################

# Describe Problem
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")
    # Problem : i can't reach to 20 because the 20 is not included.
    # Solution : Change the last range from 20 to 21


my_function()

# Reproduce the Bug
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])
# Problem here if we got the dice_num = 6 There is no index with number 6 because in list indexing starts from 0.
# Solution : Change dice_num = randint(1, 6) to dice_num = randint(1, 5)


# Play Computer
year = int(input("What's your year of birth?"))
if year >= 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")

# Fix the Errors
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

# Print is Your Friend
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)


# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
