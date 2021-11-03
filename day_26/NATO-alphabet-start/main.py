import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    print(f"{key}:{value}")

student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    # print(f"{index} {row.student}:{row.score}")
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
with open("nato_phonetic_alphabet.csv") as file:
    data = file.readlines()

data.pop(0)
print(data)
phonetic_alphabet = {word.split(",")[0]: word.split(",")[1].strip() for word in data}
print(phonetic_alphabet)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter word for translation in to NATO phonetic alphabet:").upper()
print([phonetic_alphabet[char] for char in word])
