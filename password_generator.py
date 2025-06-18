import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def evaluate_strength(password):
    length = len(password)
    has_letters = any(c.isalpha() for c in password)
    has_numbers = any(c.isdigit() for c in password)
    has_symbols = any(c in string.punctuation for c in password)

    score = sum([has_letters, has_numbers, has_symbols])

    if length < 6 or score <= 1:
        return "Weak", "red"
    elif length < 10 or score == 2:
        return "Moderate", "orange"
    else:
        return "Strong", "green"

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        characters = ""
        if var_letters.get():
            characters += string.ascii_letters
        if var_numbers.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character type.")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

        # Evaluate strength
        strength, color = evaluate_strength(password)
        strength_label.config(text=f"Strength: {strength}", fg=color)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
app = tk.Tk()
app.title("Random Password Generator")
app.geometry("350x370")
app.resizable(False, False)

tk.Label(app, text="Password Length:", font=("Arial", 12)).pack(pady=5)
length_entry = tk.Entry(app)
length_entry.pack()

tk.Label(app, text="Include:", font=("Arial", 12)).pack(pady=5)

var_letters = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(app, text="Letters (A-Z, a-z)", variable=var_letters).pack()
tk.Checkbutton(app, text="Numbers (0-9)", variable=var_numbers).pack()
tk.Checkbutton(app, text="Symbols (!@#$...)", variable=var_symbols).pack()

tk.Button(app, text="Generate Password", command=generate_password).pack(pady=10)

password_entry = tk.Entry(app, font=("Arial", 12), justify="center")
password_entry.pack(pady=5)

strength_label = tk.Label(app, text="", font=("Arial", 11))
strength_label.pack()

tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)

app.mainloop()
