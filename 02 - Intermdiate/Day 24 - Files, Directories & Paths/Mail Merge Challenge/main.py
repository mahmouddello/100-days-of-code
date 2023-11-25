# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
names_list = []
with open("./Input/Names/invited_names.txt") as names:
    for line in names:
        line = line.strip()  # removes blanks or escape character from the string
        if line == "":
            pass
        else:
            names_list.append(line)  # Appending the names from the file to a list

# OR use the readlines() method

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    content = starting_letter.read()  # Reading the starting letter
    for name in names_list:
        with open(f"./Output/ReadyToSend/letter_for_{name}", mode='w') as letters:
            letters.write(content.replace("[name]", name))  # replacing [name] placeholder in each iteration


