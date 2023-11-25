import pandas as pd

df = pd.read_csv("../../Day 26 - Comprehensions/NATO-alphabet-start/nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format: {'A':'Alfa'}
phonetic_dict = {row.letter: row.code for _, row in df.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    word = input("Name : ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(output_list)
        break
