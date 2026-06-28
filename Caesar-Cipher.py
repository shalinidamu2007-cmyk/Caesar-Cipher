def encrypt(text: str, shift: int) -> str:
    """Encrypt text using the Caesar Cipher."""
    encrypted = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char

    return encrypted


def decrypt(text: str, shift: int) -> str:
    """Decrypt text encrypted using the Caesar Cipher."""
    return encrypt(text, -shift)


def main():
    print("=== Caesar Cipher ===")

    message = input("Enter Text: ")
    shift = int(input("Enter Shift Value: "))

    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    print("\nEncrypted Text:", encrypted)
    print("Decrypted Text:", decrypted)


if __name__ == "__main__":
    main()
