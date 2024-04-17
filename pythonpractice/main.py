import tkinter as tk
from tkinter import messagebox
import new_window

def authenticate():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin":
        root.destroy()
        new_window.open_admin_page()
    else:
        messagebox.showerror("Error", "Invalid username or password")

root = tk.Tk()
root.title("Login")

# Username entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Password entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Login button
login_button = tk.Button(root, text="Login", command=authenticate)
login_button.grid(row=2, columnspan=2, pady=10)

root.mainloop()
