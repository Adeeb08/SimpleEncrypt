# Caesar Cipher Functions
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Only shift alphabet characters
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) + shift - shift_base) % 26 + shift_base)
        else:
            result += char  # Non-alphabet characters remain unchanged
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Vigenère Cipher Functions
def vigenere_encrypt(text, key):
    key = key.lower()
    result = ""
    key_index = 0
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('a')
            result += chr((ord(char) + shift - shift_base) % 26 + shift_base)
            key_index += 1
        else:
            result += char  # Non-alphabet characters remain unchanged
    return result

def vigenere_decrypt(text, key):
    key = key.lower()
    result = ""
    key_index = 0
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('a')
            result += chr((ord(char) - shift - shift_base) % 26 + shift_base)
            key_index += 1
        else:
            result += char  # Non-alphabet characters remain unchanged
    return result

# Affine Cipher function
def affine_cipher(text, a, b, m=26, mode='encrypt'):
    result = ""
    a_inv = None

    if mode == 'decrypt':
        for i in range(m):
            if (a * i) % m == 1:
                a_inv = i
                break
        if a_inv is None:
            raise ValueError("No modular inverse for the given 'a' exists.")
    
    for char in text:
        if char.isalpha():
            x = ord(char.lower()) - 97
            if mode == 'encrypt':
                result += chr(((a * x + b) % m) + 97)
            elif mode == 'decrypt':
                result += chr(((a_inv * (x - b)) % m) + 97)
        else:
            result += char
    return result


# Main Program
def main():
    print("Welcome to the Encryption/Decryption Program")
    
    while True:
        action = input("Do you want to (E)ncrypt or (D)ecrypt? (Q to quit): ").upper()
        
        if action == 'Q':
            print("Exiting the program. Goodbye!")
            break
        
        if action not in ('E', 'D'):
            print("Invalid choice! Please select E or D.")
            continue
        
        cipher_type = input("Choose the cipher (1 for Caesar, 2 for Vigenère, 3 for Affine): ")
        
        if cipher_type == '1':  # Caesar Cipher
            text = input("Enter the text: ")
            shift = int(input("Enter the shift value: "))
            
            if action == 'E':
                encrypted_text = caesar_encrypt(text, shift)
                print(f"Encrypted text (Caesar): {encrypted_text}")
            elif action == 'D':
                decrypted_text = caesar_decrypt(text, shift)
                print(f"Decrypted text (Caesar): {decrypted_text}")
        
        elif cipher_type == '2':  # Vigenère Cipher
            text = input("Enter the text: ")
            key = input("Enter the encryption key (letters only): ")
            
            if action == 'E':
                encrypted_text = vigenere_encrypt(text, key)
                print(f"Encrypted text (Vigenère): {encrypted_text}")
            elif action == 'D':
                decrypted_text = vigenere_decrypt(text, key)
                print(f"Decrypted text (Vigenère): {decrypted_text}")
        elif cipher_type == '3':  # Affine Cipher
            text = input("Enter the text: ")
            a = int(input("Enter the value of 'a' (must be coprime with 26): "))
            b = int(input("Enter the value of 'b': "))
            mode = 'encrypt' if action == 'E' else 'decrypt'
            
            try:
                result = affine_cipher(text, a, b, mode=mode)
                # Print the result for Affine cipher
                if action == 'E':
                    print(f"Encrypted text (Affine): {result}")
                else:
                    print(f"Decrypted text (Affine): {result}")
            except ValueError as e:
                print(e)
        else:
            print("Invalid cipher type! Please select 1 or 2.")
            return
        
if __name__ == "__main__":
    main()
