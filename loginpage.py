import tkinter as tk
from tkinter import messagebox
import hashlib

# Dummy user database
users = {}

def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = entry_username.get()
    password = entry_password.get()
    if username in users:
        messagebox.showerror("Error", "Username already exists!")
    else:
        users[username] = hash_password(password)
        messagebox.showinfo("Success", "Registration successful!")
        clear_entries()

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username in users and users[username] == hash_password(password):
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid credentials!")

def clear_entries():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Register and Login")

# Create the widgets
label_username = tk.Label(root, text="Username")
label_password = tk.Label(root, text="Password")
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")

button_register = tk.Button(root, text="Register", command=register)
button_login = tk.Button(root, text="Login", command=login)

# Layout the widgets
label_username.grid(row=0, column=0, padx=10, pady=10)
entry_username.grid(row=0, column=1, padx=10, pady=10)
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_password.grid(row=1, column=1, padx=10, pady=10)
button_register.grid(row=2, column=0, padx=10, pady=10)
button_login.grid(row=2, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
