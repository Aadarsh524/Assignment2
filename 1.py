def shift_text(text: str, shift: int) -> str:
    """
    Shift each letter in 'text' by 'shift' positions in the alphabet.
    Non-letter characters are left unchanged.
    """
    result = []

    for ch in text:
        if 'a' <= ch <= 'z':
            base = ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)

    return ''.join(result)


def encrypt(n: int, m: int, plaintext: str) -> str:
    """
    Encrypt 'plaintext' by shifting letters forward by (n + m).
    """
    total_shift = (n + m) % 26
    return shift_text(plaintext, total_shift)


def decrypt(n: int, m: int, ciphertext: str) -> str:
    """
    Decrypt 'ciphertext' by shifting letters backward by (n + m).
    """
    total_shift = -(n + m) % 26
    return shift_text(ciphertext, total_shift)


def main():
    # Read the text to encrypt from file
    try:
        with open("raw_text.txt", "r") as f:
            raw_content = f.read()
    except FileNotFoundError:
        print("Error: 'raw_text.txt' not found. Please create this file with your text.")
        return

    # Prompt user for integer shifts until valid
    while True:
        try:
            n = int(input("Enter integer value for n: "))
            m = int(input("Enter integer value for m: "))
            break
        except ValueError:
            print("Please enter valid integers for n and m.")

    # Perform encryption and write to file
    encrypted = encrypt(n, m, raw_content)
    with open("encrypted_text.txt", "w") as f:
        f.write(encrypted)
    print("Encryption complete. Output saved to 'encrypted_text.txt'.")

    # Decrypt and verify
    decrypted = decrypt(n, m, encrypted)
    if decrypted == raw_content:
        print("Decryption successful! The text matches the original.")
    else:
        print("Decryption failed! The text does NOT match the original.")

    # Optionally display decrypted text
    print("\nDecrypted text:")
    print(decrypted)


if __name__ == "__main__":
    main()
