# Python program to encrypt using Poly-Alphabet Cipher

# function to generate key
def generate_key(keyword):
    key = ''
    for i in range(26):
        if chr(i + 97) not in keyword:
            key += chr(i + 97)
    key = keyword + key
    return key

# function to encrypt the message
def poly_encrypt(message, key):
    encrypted_text = ''
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].isupper():
                index = ord(message[i].lower()) - 97
                encrypted_text += key[index].upper()
            else:
                index = ord(message[i]) - 97
                encrypted_text += key[index]
        else:
            encrypted_text += message[i]
    return encrypted_text

# main function
def main():
    keyword = input("Enter the keyword: ").lower()
    message = input("Enter the message: ")
    key = generate_key(keyword)
    encrypted_text = poly_encrypt(message, key)
    print("Encrypted Text: ", encrypted_text)

# calling the main function
if __name__ == '__main__':
    main()
