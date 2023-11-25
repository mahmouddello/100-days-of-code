from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(logo)


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            if new_position >= len(alphabet):
                new_position -= len(alphabet)
                end_text += alphabet[new_position]
                # if the new position of the letter over 26 we need to a circular array move by taking out the new
                # position value from the alphabet length which is 26
            elif new_position <= 0:
                new_position += len(alphabet)
                end_text += alphabet[new_position]

            else:
                end_text += alphabet[new_position]
        else:
            end_text += letter  # if the letter is a symbol don't change it just add it to the end_text
    print(f"The {cipher_direction}d text is : {end_text}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26  # to not exceed the shift limit

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type "'yes'" if you want to go again, Otherwise type "'no'"\n").lower()
    if restart == "no":
        print("Good Bye")
        should_continue = False
