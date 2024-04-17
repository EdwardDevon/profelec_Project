import tkinter as tk
from tkinter import messagebox
import admin_page
import main
from tkinter import ttk


login = tk.Tk()
login.title("Login")

#Specifying window size
app_width = 700
app_height = 400
login.resizable(False,False)
login.configure(bg="#392D69")

#Centering window based on screen size
screen_width = login.winfo_screenwidth()
screen_height = login.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height /2) - (app_height / 2)

login.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)-50}')

#Textbox Placeholder
placeholder_text = "Enter username"
placeholder_text_password = "Enter password"

def on_entry_click_username(event, entry):
    if entry.get() == placeholder_text:
        entry.delete(0, tk.END)
        entry.config(fg='black')

def on_focus_out_username(event, entry):
    if entry.get() == '':
        entry.insert(0, placeholder_text)
        entry.config(fg='grey')

def on_entry_click_password(event, entry, placeholder_text_password):
    if entry.get() == placeholder_text_password:
        entry.delete(0, tk.END)
        entry.config(fg='black')

def on_focus_out_password(event, entry, placeholder_text_password):
    if entry.get() == '':
        entry.insert(0, placeholder_text_password)
        entry.config(fg='grey')

#Check if the user is admin or cashier
def authenticate():
    username_entry = username.get()
    password_entry = password.get()

    if username_entry == "admin" and password_entry == "admin":
        login.destroy()
        admin_page.open_admin_page()

    elif username_entry == "user" and password_entry == "user":
        login.destroy()
        main.open_cashier_page()

    else:
        messagebox.showerror("Error", "Invalid username or password")





#Login Frame
frame = tk.Frame(login,width=350,height=400,bg="#fff")
frame.place(x=350,y=0)

heading1 = tk.Label(frame,text="WELCOME!",bg="#fff", fg="#392D69", font=("Helvetica", 11,'bold'))
heading1.place(x=50,y=10)
heading = tk.Label(frame,text="Sign In",bg="#fff", fg="#392D69", font=("Helvetica", 23, 'bold'))
heading.place(x=115,y=50)

#Username textbox
username = tk.Entry(frame, width=25, fg="grey", border=0,bg="#fff", font=("Poppins", 11))
username.place(x=55,y=120)
username.insert(0, placeholder_text)
username.bind("<FocusIn>", lambda event: on_entry_click_username(event, username))
username.bind("<FocusOut>", lambda event: on_focus_out_username(event, username))

tk.Frame(frame, width=250,height=2,bg="black",border=0).place(x=50,y=150)

#Password textbox
password = tk.Entry(frame, width=25, fg="grey", border=0,bg="#fff",font=("Poppins", 11))
password.place(x=55,y=190)
password.insert(0,placeholder_text_password)
password.bind("<FocusIn>", lambda event: on_entry_click_password(event,password,placeholder_text_password))
password.bind("<FocusOut>",lambda event:on_focus_out_password(event,password,placeholder_text_password))

tk.Frame(frame, width=250,height=2,bg="black").place(x=50,y=220)

#Submit button
button = tk.Button(frame,width=19,pady=5, text="SUBMIT", fg="#fff",bg="#57a1f8",border=0,command=authenticate)
button.place(x=105,y=250)





login.mainloop()