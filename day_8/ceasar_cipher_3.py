alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(cipher_text, shift_amount,direction_encryption):
    decrypted_text = ""
    position = 0
    if direction_encryption == "decode":
        for char in cipher_text:
            position = alphabet.index(char)
            if position - shift >= 0:
                decrypted_text += alphabet[position-shift_amount]
            else:
                position = len(alphabet) - (abs(position - shift_amount) % len(alphabet))
                decrypted_text += alphabet[position]
        print(f'The decoded text is: {decrypted_text}')
    elif direction_encryption == "encode":
        for char in cipher_text:
            position = alphabet.index(char)
            #print(f"{position+shift_amount}:{len(alphabet)}")
            if position + shift_amount < len(alphabet):
                decrypted_text += alphabet[position+shift_amount]
            else:
                position = (position + shift_amount) % len(alphabet)
                decrypted_text += alphabet[position]
        print(f'The encodeed text is: {decrypted_text}')
    else:
        print("You suck.n\Betty had eyes that said come here, lips that said kiss me, arms and torso that said hold me all night long, but the rest of her body said, “Fillet me, cover me in cornmeal, and fry me in peanut oil”; romance wasn’t easy for a mermaid.")

'''
def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")
'''

'''
if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(cipher_text=text, shift_amount=shift)
'''

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(text,shift,direction)