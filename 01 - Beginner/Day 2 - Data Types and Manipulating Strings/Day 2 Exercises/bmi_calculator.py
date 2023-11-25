# BMI stands for : Body mass index
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height.
# e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

height = input("entre your height in m: ")
weight = input("entre your weight in kg: ")
# taking inputs from the user
int_height = float(height)
int_weight = float(weight)

BMI = int(int_weight / int_height**2)

print(BMI)
