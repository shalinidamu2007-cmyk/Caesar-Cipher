# Caesar Cipher Encryption and Decryption

A simple Python implementation of the **Caesar Cipher**, one of the oldest and most well-known substitution encryption techniques. This project allows users to encrypt and decrypt text using a user-defined shift value.

## Features

- Encrypts plaintext using the Caesar Cipher algorithm.
- Decrypts ciphertext back to the original message.
- Supports both uppercase and lowercase letters.
- Preserves spaces, numbers, and special characters.
- User-defined shift value.

## Technologies Used

- Python 3

## Project Structure

```
Caesar-Cipher/
│── caesar_cipher.py
│── README.md
```

## How It Works

The Caesar Cipher shifts each alphabetic character by a fixed number of positions in the alphabet.

Example with a shift value of **3**:

```
Plain Text : HELLO
Encrypted : KHOOR
Decrypted : HELLO
```

## Installation

1. Clone the repository.

```bash
git clone https://github.com/your-username/Caesar-Cipher.git
```

2. Navigate to the project directory.

```bash
cd Caesar-Cipher
```

3. Run the program.

```bash
python caesar_cipher.py
```

## Sample Output

```
=== Caesar Cipher ===

Enter Text: Hello World
Enter Shift Value: 3

Encrypted Text: Khoor Zruog
Decrypted Text: Hello World
```

## Algorithm

1. Read the input text.
2. Read the shift value.
3. Encrypt each alphabetic character by shifting it forward.
4. Leave non-alphabetic characters unchanged.
5. Decrypt by shifting the encrypted text backward.
6. Display both encrypted and decrypted text.

## Applications

- Learning basic cryptography
- Information security fundamentals
- Educational demonstrations
- Understanding substitution ciphers

## Future Enhancements

- Graphical User Interface (GUI)
- File encryption and decryption
- Brute-force attack demonstration
- Support for multiple cipher algorithms

## 👩‍💻 Author

**Shalini D**

Cyber Security Intern

DecodeLabs Industrial Training Program
## License

This project is licensed under the MIT License.
