import random
import tkinter as tk

def generate_password():
    password_length = int(input("Enter length for password"))
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text=password)

window = tk.Tk()
window.title("Password Generator")

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(window, text="Click button to generate password", font=("Arial", 12))
password_label.pack(pady=10)

window.mainloop()