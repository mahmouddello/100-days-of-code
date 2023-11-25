print("Welcome to the roller coaster")
height = int(input("What is your height in cm? "))

if height > 120:  # True
    print("You can ride the roller coaster!")
    age = int(input("How old are you? "))
    if age < 12:
        print("please pay $5.")
    elif age <= 18:
        print("please pay $7.")
    else:
        print("please pay 12$.")
    # End of inner if - else
else:  # False
    print("Sorry, you have to grow taller before you can ride.")
# End of outer if - else

