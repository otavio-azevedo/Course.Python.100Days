from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    encoded_text = ""
    last_index_alphabet = len(alphabet)

    for letter in text:
        shifted_index = alphabet.index(letter)+shift

        if(shifted_index == last_index_alphabet):
            shifted_index = 0

        encoded_text += alphabet[shifted_index]

    return encoded_text


def decrypt(text, shift):
    negative_shift = shift*-1
    return encrypt(text=text, shift=negative_shift)


print(logo)

direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

result = ""
if(direction == "encode"):
    result = encrypt(text, shift)
elif (direction == "decode"):
    result = decrypt(text, shift)
else:
    print("Invalid option 😑")
    exit(1)

print(f"Original Text: {text} ➡️")
print(f"Final Text: {result} ⬅️")
