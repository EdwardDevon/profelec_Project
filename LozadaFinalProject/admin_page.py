import tkinter as tk


def open_admin_page():
    admin_page = tk.Tk()
    admin_page.title("Admin Page")

    #Specifying window size
    app_width = 1200
    app_height = 600
    admin_page.resizable(False,False)
    admin_page.configure(bg="#fff")

    #Centering window based on screen size
    screen_width = admin_page.winfo_screenwidth()
    screen_height = admin_page.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height /2) - (app_height / 2)

    admin_page.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)-50}')

    left_col = tk.Frame(admin_page,width=200,height=650,bg="grey")
    left_col.place(x=0,y=0)

    heading_row = tk.Frame(admin_page,width=995,height=100,bg="#9CAFAA")
    heading_row.place(x=205,y=0)











    admin_page.mainloop()


if __name__ == "__main__":
    open_admin_page()