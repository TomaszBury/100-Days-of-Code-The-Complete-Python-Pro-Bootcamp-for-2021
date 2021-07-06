alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    text_encrypted = []
    k = 0
    for char in plain_text:
        k = alphabet.index(char)
        #print(f"{k+shift_amount}:{len(alphabet)}")
        if k + shift_amount < len(alphabet):
            text_encrypted.append(alphabet[k+shift_amount])
        else:
            k = (k + shift_amount) % len(alphabet)
            text_encrypted.append(alphabet[k])

    print(f'The encoded text is: {"".join(text_encrypted)}')

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

def decrypt(text, shift):
    decrypted_text = ""
    position = 0
    for char in text:
        position = alphabet.index(char)
        if position - shift >= 0:
            decrypted_text += alphabet[position-shift]
        else:
            position = len(alphabet) - (abs(position - shift) % len(alphabet))
            decrypted_text += alphabet[position]
    print(f'The decoded text is: {decrypted_text}')

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(text,shift)
else:
    print("'encode' to encrypt, type 'decode' to decrypt is this that hard?\n =-=-=-=-=-=-=-=-=-===-=-\nSeflf Termination.")