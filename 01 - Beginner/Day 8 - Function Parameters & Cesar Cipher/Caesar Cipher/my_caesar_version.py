alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


#########################
# 1) Encryption :
# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount
#  and print the encrypted text. e.g. plain_text = "hello" shift = 5 cipher_text = "mjqqt" print output: "The encoded
#  text is mjqqt"

# HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)  # returns position of the current letter in the plain text
        new_position = shift_amount + position  # the new position of the letter to do encrypt operation
        if new_position >= len(alphabet):  # if the new position get out of range
            new_position -= len(alphabet)
            # subtract the length of the alphabet from the new position , so it goes backwards
            new_letter = alphabet[new_position]  # now the new letter is an encrypted letter in the specific position
            cipher_text += new_letter  # adding our new letter to the string
        else:
            # do every thing normally
            new_letter = alphabet[new_position]
            cipher_text += new_letter
    print(f"The encrypted text : {cipher_text}")  # print the encrypted text


#########################
# 2) Decryption :
# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift
#  amount and print the decrypted text. e.g. cipher_text = "mjqqt" shift = 5 plain_text = "hello" print output: "The
#  decoded text is hello"
end_program = False


def decrypt(encrypted_text, shift_amount):
    decrypted_text = ""
    for letter in encrypted_text:
        position = alphabet.index(letter)  # returns position of the current letter in the plain text
        new_position = position - shift_amount  # the new position of the letter to do decrypt operation
        if new_position <= 0:  # if the new position get out of range (from beginning because we're counting backwards)
            new_position += len(alphabet)  # add the length of the alphabet to the new position, so it goes forwards
            new_letter = alphabet[new_position]  # now the new letter is an encrypted letter in the specific position
            decrypted_text += new_letter  # print the encrypted text
        else:
            new_letter = alphabet[new_position]
            decrypted_text += new_letter
    print(f"The decrypted text : {decrypted_text}")


#########################

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

while not end_program:
    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(encrypted_text=text, shift_amount=shift)
    else:
        print("Wrong input, shutting down program !")
        end_program = True
