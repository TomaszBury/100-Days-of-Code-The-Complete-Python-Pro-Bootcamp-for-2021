import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛 or zulu

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

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

encrypt(plain_text=text,shift_amount=shift)