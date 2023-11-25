import pandas

user_name = input("What's your name? ").upper()

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato = [row.code for letter in user_name for (index, row) in data.iterrows() if row.letter == letter]
print(nato)
