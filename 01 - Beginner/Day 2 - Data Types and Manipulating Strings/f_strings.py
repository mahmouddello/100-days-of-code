score = 0
height = 1.8
isWinning = True
# Instead of writing these stuffs with too much + signs it is really complicated
print("your score is = "+str(score)+", your height = "+str(height)+", your winning possibility is "+str(isWinning))
# We need something that's more efficient, so we use a way called (f-strings)

# F-String :
# we add the 'f' character in front of the string (double quotes) and now,
# we can start adding various values into the string
print(f"Your score is {score}, your height is {height}, your winning possibility is {isWinning}")
