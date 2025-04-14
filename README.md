# SimpleEncrypt

## Description
**SimpleEncrypt** is a user-friendly Python tool with a graphical interface that allows users to encrypt and decrypt messages using classical cipher techniques. Built with Tkinter, it provides a smooth experience for experimenting with encryption methods.

## Ciphers Implemented

- **Caesar Cipher** – Shifts each letter in the plaintext by a fixed number of positions in the alphabet.

- **Vigenère Cipher** – Uses a keyword to apply different Caesar shifts to each character of the message.

- **Affine Cipher** – Applies a mathematical function of the form **(a * x + b) mod m**, where:
  - **x** is the position of the letter in the alphabet,
  - **a** and **b** are keys,
  - **m** is the size of the alphabet (typically 26 for English letters).

> *More ciphers will be added in future updates.*

## Technologies Used
- Python
- Tkinter (for GUI)

## Files
- `simpleencrypt.py`: Main GUI-based encryption tool.
- `prototype1.py`: First version of the program using command-line interaction (no GUI).

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/Adeeb08/SimpleEncrypt.git

2. Navigate to the project directory:
   ```bash
   cd SimpleEncrypt

3. Run the GUI application:
   ```bash
   python simpleencrypt.py

4. Use the interface to:

   a. Select a cipher.

   b. Enter your message and keys.

   c. Encrypt or decrypt text.

   d. Copy the result to your clipboard.




**NOTE** : This project uses **TKINTER**, which is included with most standard Python installation. If it's missing, you can install it on **Linux** (Debian-based) using 'sudo apt install python3-tk'. On **Windows**, you can ensure that tkinter module is selected during Python installation.
