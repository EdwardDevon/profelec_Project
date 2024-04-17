import tkinter as tk

def check_credentials():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin":
        open_new_window()
    else:
        error_label.config(text="Invalid username or password")

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Welcome")
    tk.Label(new_window, text="Welcome, Admin!", font=("Helvetica", 16)).pack(padx=20, pady=10)

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
login_button = tk.Button(root, text="Login", command=check_credentials)
login_button.grid(row=2, columnspan=2, pady=10)

# Error message label
error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=3, columnspan=2)

root.mainloop()
