# kriptografi3
 Poly-Alphabet


  # Polyalphabet
     Cipher Polyalphabet (juga dikenal sebagai Cipher Polyalphabetic) adalah salah satu jenis teknik enkripsi dalam ilmu kriptografi. Ini adalah metode enkripsi yang menggunakan beberapa alfabet (seringkali disebut sebagai tabel alfabet) yang berbeda untuk mengenkripsi teks. Ide dasar dari Cipher Polyalphabet adalah menggeser karakter-karakter dalam teks asli dengan alfabet yang berbeda berdasarkan aturan tertentu, yang dapat bervariasi sesuai dengan implementasinya.

    Pada umumnya, dalam Cipher Polyalphabet, setiap karakter dalam teks asli digeser atau diubah dengan alfabet yang berbeda berdasarkan posisi karakter dalam teks dan kunci enkripsi yang digunakan. Kunci ini dapat berupa kata atau frase tertentu yang digunakan untuk mengontrol pergeseran alfabet.

    Salah satu bentuk paling terkenal dari Cipher Polyalphabet adalah Cipher Vigenère, di mana pergeseran alfabet diatur oleh kata kunci yang berulang. Setiap huruf dalam kata kunci digunakan untuk menggeser alfabet dengan jumlah yang sesuai, dan ini akan diulang terus menerus sepanjang teks.

    Cipher Polyalphabet memiliki tingkat keamanan yang lebih tinggi daripada beberapa teknik enkripsi sederhana, seperti Caesar Cipher, karena pergeseran alfabet yang bervariasi membuat analisis frekuensi karakter menjadi lebih sulit. Namun, seperti semua teknik enkripsi, keamanan Polyalphabet Cipher tergantung pada panjang dan kompleksitas kunci, serta kemampuan menganalisis teks terenkripsi.








  ```php
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

```

# Penjelasan 
* def polyalphabet_cipher(plaintext, key):: Ini adalah definisi fungsi polyalphabet_cipher yang menerima dua parameter, yaitu plaintext (teks yang akan dienkripsi) dan key (kunci enkripsi).

* plaintext = plaintext.upper().replace(" ", "").replace(".", "").replace(",", ""): Teks plaintext diubah menjadi huruf kapital (uppercase) dengan .upper() dan kemudian dilakukan penghapusan spasi, titik, dan koma menggunakan .replace(). Ini dilakukan untuk membersihkan teks dari karakter-karakter yang tidak relevan dalam proses enkripsi.

* alphabets = []: Variabel alphabets inisialisasi sebagai sebuah daftar kosong yang akan digunakan untuk menyimpan alfabet-alfabet yang sudah di-shift sesuai dengan kunci.

* for i in range(len(key)):: Ini adalah awal dari loop for yang akan mengiterasi melalui setiap karakter dalam kunci key.

* shift = ord(key[i]) - 65: Di dalam loop, karakter kunci diubah menjadi nilai pergeseran (shift) dengan mengambil kode Unicode dari karakter tersebut (ord(key[i])) dan menguranginya dengan 65 (nilai ASCII untuk huruf 'A'). Ini menghasilkan nilai pergeseran antara 0 hingga 25.

* alphabet = [chr((j + shift) % 26 + 65) for j in range(26)]: Untuk setiap nilai pergeseran, daftar alfabet baru dibuat dengan menggeser setiap huruf di alfabet asli sebanyak shift langkah. Kode ini menghasilkan alfabet yang di-shift sesuai dengan kunci dan disimpan dalam alphabets.

* ciphertext = "": Variabel ciphertext digunakan untuk menyimpan teks hasil enkripsi yang akan dibangun selama proses enkripsi.

* for i in range(len(plaintext)):: Ini adalah loop yang mengiterasi melalui setiap karakter dalam teks plaintext yang sudah dibersihkan.

* alphabet_index = i % len(key): Ini digunakan untuk menentukan indeks alfabet yang akan digunakan saat ini berdasarkan iterasi yang sedang dilakukan dan panjang kunci. Hal ini memungkinkan kita untuk bergantian menggunakan alfabet-alfabet yang sesuai dengan kunci.

* alphabet = alphabets[alphabet_index]: Kita mengambil alfabet yang sesuai dengan indeks yang telah dihitung sebelumnya.

* letter_index = ord(plaintext[i]) - 65: Kami mengambil indeks karakter saat ini dalam alfabet asli dengan mengonversi karakter ke kode Unicode (ord(plaintext[i])) dan menguranginya dengan 65 (nilai ASCII untuk huruf 'A').

* ciphertext += alphabet[letter_index]: Kami mengambil karakter yang sesuai dari alfabet yang telah di-shift dan menambahkannya ke ciphertext. Ini adalah bagian dari proses enkripsi.

* return ciphertext: Hasil enkripsi akhir dikembalikan dari fungsi sebagai ciphertext.



