import tkinter as tk
from tkinter import Label, Entry, Button, Text, Scrollbar

def caesar_encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            if not is_upper:
                shifted_char = shifted_char.lower()
            encrypted_text += shifted_char
        else:
            encrypted_text += char

    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = caesar_encrypt(encrypted_text, -shift)
    return decrypted_text

def encrypt_text():
    shift = int(shift_entry.get())
    plain_text = plaintext_entry.get()
    encrypted_text = caesar_encrypt(plain_text, shift)
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, encrypted_text)
    result_text.config(state=tk.DISABLED)

def decrypt_text():
    shift = int(shift_entry.get())
    encrypted_text = plaintext_entry.get()
    decrypted_text = caesar_decrypt(encrypted_text, shift)
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, decrypted_text)
    result_text.config(state=tk.DISABLED)

app = tk.Tk()
app.title("Caesar密码工具")

shift_label = Label(app, text="位移值:")
shift_label.pack()
shift_entry = Entry(app)
shift_entry.pack()

plaintext_label = Label(app, text="文本:")
plaintext_label.pack()
plaintext_entry = Entry(app)
plaintext_entry.pack()

encrypt_button = Button(app, text="加密", command=encrypt_text)
encrypt_button.pack()

decrypt_button = Button(app, text="解密", command=decrypt_text)
decrypt_button.pack()

result_label = Label(app, text="结果:")
result_label.pack()
result_text = Text(app, height=6, width=30)
result_text.config(state=tk.DISABLED)
result_text.pack()

scrollbar = Scrollbar(app, command=result_text.yview)
scrollbar.pack()
result_text.config(yscrollcommand=scrollbar.set)

app.mainloop()


