alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def cesar(plain_text, shift_amount, user_direction):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if user_direction == 'encode':
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
            print(f"The encoded text is {cipher_text}")
        elif user_direction == 'decode':
            new_position = position - shift_amount
            cipher_text += alphabet[new_position]
            print(f"The decoded text is {cipher_text}")


cesar(plain_text=text, shift_amount=shift, user_direction=direction)
