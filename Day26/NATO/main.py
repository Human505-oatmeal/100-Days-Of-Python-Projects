import pandas
new_df = pandas.read_csv("nato_phonetic_alphabet.csv")
new_storage = {row.letter: row.code for (index, row) in new_df.iterrows()}
x = input("Enter a word: ").upper()
output = [new_storage[item] for item in x]
print(output)
