# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as file:
    list_of_names = file.readlines()
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter_template = starting_letter.read()


count = 0
for name in list_of_names:
    count += 1
    print(f"Line{count}: {name.strip()}")
    new_letter = letter_template.replace("[name]", name.strip())
    with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as letter:
        letter.write(f"{new_letter}")


