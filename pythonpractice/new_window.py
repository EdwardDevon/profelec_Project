import tkinter as tk

def open_admin_page():
    admin_window = tk.Toplevel()
    admin_window.title("Admin Page")

    # Add widgets to the admin page
    label = tk.Label(admin_window, text="Welcome, Admin!")
    label.pack(padx=20, pady=10)

    # Add more widgets as needed

    admin_window.mainloop()

# Run the admin page directly when this file is executed
if __name__ == "__main__":
    open_admin_page()
