text = 'Hello Zaira'
shift = 3
custom_key = 'python'

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

def vigenere(message, key):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        # Append space to the message
        if char == ' ':
            encrypted_text += char
        else:
            #finding new key character
            key_char = key[key_index % len(key)]
            key_index += 1
            #define the offset
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    return encrypted_text

caesar(text, shift)
caesar(text, 13)
encryption = vigenere(text,custom_key)
print(encryption)