import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Clean Cipher Tool")

# Cipher functions
def caesar_encrypt(text, shift):
    return ''.join(chr((ord(char) - ord('a') + shift) % 26 + ord('a')) if char.isalpha() else char for char in text.lower())

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def vigenere_encrypt(text, key):
    key = key.lower()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            result += chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    key = key.lower()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            result += chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
            key_index += 1
        else:
            result += char
    return result

def affine_cipher(text, a, b, mode='encrypt'):
    m = 26
    result = ''
    a_inv = None
    if mode == 'decrypt':
        for i in range(m):
            if (a * i) % m == 1:
                a_inv = i
                break
        if a_inv is None:
            raise ValueError("No inverse for a exists.")
    for char in text:
        if char.isalpha():
            x = ord(char.lower()) - ord('a')
            if mode == 'encrypt':
                result += chr(((a * x + b) % m) + ord('a'))
            else:
                result += chr(((a_inv * (x - b)) % m) + ord('a'))
        else:
            result += char
    return result

# GUI logic
def update_fields(*args):
    # Hide all
    shift_frame.grid_remove()
    key_frame.grid_remove()
    affine_frame.grid_remove()

    cipher = cipher_var.get()
    if cipher == "Caesar":
        shift_frame.grid(row=4, column=0, columnspan=2, pady=5)
    elif cipher == "Vigenère":
        key_frame.grid(row=4, column=0, columnspan=2, pady=5)
    elif cipher == "Affine":
        affine_frame.grid(row=4, column=0, columnspan=2, pady=5)

def process():
    text = input_text.get("1.0", "end-1c")
    action = action_var.get()
    cipher = cipher_var.get()
    try:
        if cipher == "Caesar":
            shift = int(shift_entry.get())
            result = caesar_encrypt(text, shift) if action == "Encrypt" else caesar_decrypt(text, shift)
        elif cipher == "Vigenère":
            key = key_entry.get()
            result = vigenere_encrypt(text, key) if action == "Encrypt" else vigenere_decrypt(text, key)
        elif cipher == "Affine":
            a = int(a_entry.get())
            b = int(b_entry.get())
            result = affine_cipher(text, a, b, mode='encrypt' if action == "Encrypt" else 'decrypt')
        output_text.config(state="normal")
        output_text.delete("1.0", "end")
        output_text.insert("1.0", result)
        output_text.config(state="disabled")
        copy_button.grid(row=7, column=1)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def copy_output():
    result = output_text.get("1.0", "end-1c")
    root.clipboard_clear()
    root.clipboard_append(result)
    messagebox.showinfo("Copied", "Output copied to clipboard!")

# Widgets
cipher_var = tk.StringVar(value="Caesar")
cipher_var.trace_add("write", update_fields)

action_var = tk.StringVar(value="Encrypt")

tk.Label(root, text="Select Cipher:").grid(row=0, column=0, sticky="w")
tk.OptionMenu(root, cipher_var, "Caesar", "Vigenère", "Affine").grid(row=0, column=1, sticky="ew")

tk.Label(root, text="Action:").grid(row=1, column=0, sticky="w")
tk.Radiobutton(root, text="Encrypt", variable=action_var, value="Encrypt").grid(row=1, column=1, sticky="w")
tk.Radiobutton(root, text="Decrypt", variable=action_var, value="Decrypt").grid(row=1, column=1)

tk.Label(root, text="Input Text:").grid(row=2, column=0, sticky="w")
input_text = tk.Text(root, height=4, width=40)
input_text.grid(row=3, column=0, columnspan=2)

# Caesar
shift_frame = tk.Frame(root)
tk.Label(shift_frame, text="Shift:").pack(side="left")
shift_entry = tk.Entry(shift_frame)
shift_entry.pack(side="left")

# Vigenere
key_frame = tk.Frame(root)
tk.Label(key_frame, text="Key:").pack(side="left")
key_entry = tk.Entry(key_frame)
key_entry.pack(side="left")

# Affine
affine_frame = tk.Frame(root)
tk.Label(affine_frame, text="a:").pack(side="left")
a_entry = tk.Entry(affine_frame, width=5)
a_entry.pack(side="left")
tk.Label(affine_frame, text="b:").pack(side="left")
b_entry = tk.Entry(affine_frame, width=5)
b_entry.pack(side="left")

# Output
tk.Button(root, text="Go", command=process).grid(row=6, column=0, pady=5)
copy_button = tk.Button(root, text="Copy", command=copy_output)
output_text = tk.Text(root, height=4, width=40, state="disabled")
output_text.grid(row=6, column=1)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_output)
copy_button.grid(row=7, column=1, pady=5)

update_fields()  # Initial hide of unused fields

root.mainloop()
