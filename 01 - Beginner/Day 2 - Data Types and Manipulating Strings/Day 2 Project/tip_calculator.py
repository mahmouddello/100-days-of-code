# Instructions :
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
##########################################
print("Welcome to the tip calculator.")  # Welcome message
bill = float(input("What was the total bill? $"))  # converting string to int
tip = int(input("What percentage tip would you like to give? 10%, 12%, or 15%?"))  # converting string to int
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill  # the bill after we add the tip! not the tip percentage !!
# bill_with_tip = bill * (1 + tip / 100) this will also give us same result
print(f"The new total of the bill is = {bill_with_tip}")  # new total of the bill after finish adding the tip
bill_per_person = round(bill_with_tip / people, 2)  # after getting the result rounding it to 2 decimal places
# Example if the result = 33.62 we round it to two decimal places so new result will be 33.60
print(f"Each person should pay ${bill_per_person}")
# if you want to show two decimal places you should use a new sort of format
bill_per_person = "{:.2f}".format(bill_per_person)  # specifying how many numbers after the decimal place
print(f"Each person should pay ${bill_per_person}")
###########################################



