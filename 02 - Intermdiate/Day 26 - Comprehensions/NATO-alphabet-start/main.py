import pandas as pd

# TODO 1. Create a dictionary in this format:

df = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for _, row in df.iterrows()}
print(phonetic_dict)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Name : ").upper()
output_list = [phonetic_dict[letter] for letter in word]
# each letter in the word is the key to access to the corresponding value
print(output_list)

# phonetic_dictionary["letter"] will look for a key called "letter" and return the value at that key
# (if it exists).
#
# But in the code output = [phonetic_dictionary[letter] for letter in word],
# we are using letter as a variable.
#
# Your NATO dictionary looks like this:
#
# phonetic_dictionary = {
#     'A': 'Alfa',
#     'B': 'Bravo',
#     'C': 'Charlie',
#     ...
# }
# Let's say word = "cab".
#
# In our code, output = [phonetic_dictionary[letter] for letter in word]
#
# letter first takes on the value "c". The first value of the output list will be
#
# phonetic_dictionary[letter] = phonetic_dictionary["c"] = "Charlie"
#
# So now output = ["Charlie"]
#
# Now we get the next letter in word. letter now has the value "a",
# and the next value of the output list will be
#
# phonetic_dictionary[letter] = phonetic_dictionary["a"] = "Alfa"
#
# So now output = ["Charlie", "Alfa"]
#
# and so on.