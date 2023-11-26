import pandas as pd


df = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for _, row in df.iterrows()}
print(phonetic_dict)

word = input("Name : ").upper()
output_list = [phonetic_dict[letter] for letter in word]
# each letter in the word is the key to access to the corresponding value
print(output_list)

# Phonetic_dictionary["letter"] will look for a key called "letter" and return the value at that key
# (if it exists).
#
# But in the code output = [phonetic_dictionary[letter] for a letter in word],
# we are using a letter as a variable.
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
# In our code, output = [phonetic_dictionary[letter] for a letter in word]
#
# letter first takes on the value "c". The first value of the output list will be
#
# phonetic_dictionary[letter] = phonetic_dictionary["c"] = "Charlie"
#
# So now output = ["Charlie"]
#
# Now we get the next letter in word. Letter now has the value "a",
# and the next value of the output list will be
#
# phonetic_dictionary[letter] = phonetic_dictionary["a"] = "Alfa"
#
# So now output = ["Charlie", "Alfa"]
#
# and so on.
