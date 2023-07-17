import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

Nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(Nato_dict)


def nato_conver():
    user_input = input("Enter your name:").upper()
    try:
        words = [Nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Only letters are allowed")
        nato_conver()
    else:
        print(words)


nato_conver()