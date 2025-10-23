import numpy as np

def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text.upper().replace(" ", "")]

def numbers_to_text(numbers):
    return ''.join(chr(int(n) + ord('A')) for n in numbers)

def hill_encrypt(plaintext, key_matrix):
    n = key_matrix.shape[0]
    plaintext_numbers = text_to_numbers(plaintext)
   
    while len(plaintext_numbers) % n != 0:
        plaintext_numbers.append(ord('X') - ord('A'))
    
    ciphertext = []
    for i in range(0, len(plaintext_numbers), n):
        block = np.array(plaintext_numbers[i:i+n])
        enc_block = np.dot(key_matrix, block) % 26
        ciphertext.extend(enc_block)
    
    return numbers_to_text(ciphertext)

def hill_decrypt(ciphertext, key_matrix):
    n = key_matrix.shape[0]
    cipher_numbers = text_to_numbers(ciphertext)
    
    det = int(round(np.linalg.det(key_matrix))) % 26
    det_inv = pow(det, -1, 26)  

    key_matrix_inv = (
        det_inv * np.round(det * np.linalg.inv(key_matrix)).astype(int)
    ) % 26

    plaintext = []
    for i in range(0, len(cipher_numbers), n):
        block = np.array(cipher_numbers[i:i+n])
        dec_block = np.dot(key_matrix_inv, block) % 26
        plaintext.extend(dec_block)
    
    return numbers_to_text(plaintext)

if __name__ == "__main__":
    key_matrix = np.array([[3, 3],
                           [2, 5]])  
    plaintext = input("Masukkan plaintext: ").upper()

    ciphertext = hill_encrypt(plaintext, key_matrix)
    decrypted = hill_decrypt(ciphertext, key_matrix)

    print("\n=== HASIL ===")
    print("Plaintext  :", plaintext)
    print("Ciphertext :", ciphertext)
    print("Dekripsi   :", decrypted)
