def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift 
    
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result


message = input("Enter a message: ")
shift = int(input("Enter shift value (1-25): "))
action = input("Encrypt or decrypt? (e/d): ").lower()

if action == 'e':
    encrypted = caesar_cipher(message, shift)
    print("Encrypted:", encrypted)
elif action == 'd':
    decrypted = caesar_cipher(message, shift, 'decrypt')
    print("Decrypted:", decrypted)
else:
    print("any choice. Use 'e' or 'd'.")
    


 