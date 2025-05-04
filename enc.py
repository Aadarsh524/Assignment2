def encrypt_char(char, n, m):
    """Encrypt a single character based on the specified rules."""
    if char.islower():
        if 'a' <= char <= 'm':
            shift = (n * m) % 26
            pos = (ord(char) - ord('a') + shift) % 26
            return chr(ord('a') + pos)
        elif 'n' <= char <= 'z':
            shift = (n + m) % 26
            pos = (ord(char) - ord('a') - shift) % 26
            return chr(ord('a') + pos)
    elif char.isupper():
        if 'A' <= char <= 'M':
            shift = n % 26
            pos = (ord(char) - ord('A') - shift) % 26
            return chr(ord('A') + pos)
        elif 'N' <= char <= 'Z':
            shift = (m ** 2) % 26
            pos = (ord(char) - ord('A') + shift) % 26
            return chr(ord('A') + pos)
    return char
    

def encrypt_text(text, n, m):
    """Encrypt the entire text."""
    return ''.join(encrypt_char(c, n, m) for c in text)

if __name__ == "__main__":
    try:
        n = int(input("Enter n: "))
        m = int(input("Enter m: "))
    except ValueError:
        print("Please enter integers for n and m.")
        exit(1)

    # Read original text from file
    with open("raw_text.txt", "r", encoding='utf-8') as file:
        original_text = file.read()

    # Encrypt the text
    encrypted_text = encrypt_text(original_text, n, m)

    # Write encrypted text to a new file
    with open("encrypted_text.txt", "w", encoding='utf-8') as file:
        file.write(encrypted_text)

    print("Encryption complete. See 'encrypted_text.txt'.")
