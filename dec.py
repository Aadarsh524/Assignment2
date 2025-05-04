# decryption.py
"""
Defines routines to decrypt and verify output of encryption.py.

  • decrypt_char: reverses the two-parameter cipher for a single character.
  • decrypt_text: applies decrypt_char across the encrypted string.
  • check_decryption: compares decrypted text against 'raw_text.txt'.
"""
def decrypt_char(char, n, m):
        """Decrypt a single character based on the specified rules."""
        if char.islower():
            if 'a' <= char <= 'm':
                shift = (n * m) % 26
                pos = (ord(char) - ord('a') - shift) % 26
                return chr(ord('a') + pos)
            elif 'n' <= char <= 'z':
                shift = (n + m) % 26
                pos = (ord(char) - ord('a') + shift) % 26
                return chr(ord('a') + pos)
        elif char.isupper():
            if 'A' <= char <= 'M':
                shift = n % 26
                pos = (ord(char) - ord('A') + shift) % 26
                return chr(ord('A') + pos)
            elif 'N' <= char <= 'Z':
                shift = (m ** 2) % 26
                pos = (ord(char) - ord('A') - shift) % 26
                return chr(ord('A') + pos)
        return char

def decrypt_text(text, n, m):
        """Decrypt the entire text."""
        return ''.join(decrypt_char(c, n, m) for c in text)

def check_correctness(original_text, decrypted_text):
        """Check if the decrypted text matches the original text."""
        return original_text == decrypted_text

if __name__ == '__main__':
    try:
        n = int(input("Enter shift value n (for decryption): "))
        m = int(input("Enter shift value m (for decryption): "))
    except ValueError:
        print("Please enter integer values for n and m.")
        exit(1)

    # Read encrypted data
    with open('encrypted_text.txt', 'r', encoding='utf-8') as fin:
        enc = fin.read()

    # Decrypt entire text
    dec = decrypt_text(enc, n, m)

    # Write decrypted output
    with open('decrypted_text.txt', 'w', encoding='utf-8') as fout:
        fout.write(dec)
    print("Decryption complete. See 'decrypted_text.txt'.")

    # Verify correctness
    if check_correctness('raw_text.txt', dec):
        print("Success: decrypted text matches original.")
    else:
        print("Warning: decrypted text does NOT match original.")
