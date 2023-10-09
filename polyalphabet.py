def polyalphabet_cipher(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "").replace(".", "").replace(",", "")
    alphabets = []
    for i in range(len(key)):
        shift = ord(key[i]) - 65
        alphabet = [chr((j + shift) % 26 + 65) for j in range(26)]
        alphabets.append(alphabet)
    ciphertext = ""
    for i in range(len(plaintext)):
        alphabet_index = i % len(key)
        alphabet = alphabets[alphabet_index]
        letter_index = ord(plaintext[i]) - 65
        ciphertext += alphabet[letter_index]
    return ciphertext

plaintext = input("Masukkan teks yang akan dienkripsi: ")
key = "selasa"
ciphertext = polyalphabet_cipher(plaintext, key)
print("Hasil enkripsi:", ciphertext)
