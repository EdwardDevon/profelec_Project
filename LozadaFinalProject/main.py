import tkinter as tk

def open_cashier_page():
    main= tk.Tk()
    main.title("Cashier Page")
    main.padding = 20   

    #Specifying window size
    app_width = 1300
    app_height = 650
    main.resizable(False,False)
    main.configure(bg="pink")

    #Centering window based on screen size
    screen_width =main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height /2) - (app_height / 2)

    main.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)-50}')

    #User Profile frame
    profile_frame = tk.Frame(main, width=200,height=650,bg="#222831")
    profile_frame.pack(side="left", padx=10, pady=10)


    #Product List frame
    product_frame =  tk.Frame(main,width=500,height=650,bg="#F5EEE6")
    product_frame.pack(side="left", padx=10, pady=10)   



    #Order Status Frame
    order_status_frame =  tk.Frame(main,width=300,height=650,bg="blue")
    order_status_frame.pack(side="left", padx=10, pady=10)



    #Receipt Frame
    receipt_frame =  tk.Frame(main,width=230,height=650,bg="red")
    receipt_frame.pack(side="left", padx=10, pady=10)








    main.mainloop()


if __name__ == "__main__":
    open_cashier_page()