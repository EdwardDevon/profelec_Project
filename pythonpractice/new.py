import tkinter as tk


def resize_image(img, factor):
    return img.subsample(factor)

def display_resized_images(root, image_paths, factor):
    for image_path in image_paths:
        try:
            img = tk.PhotoImage(file=image_path)
            img_resized = resize_image(img, factor)
            label = tk.Label(root, image=img_resized)
            label.pack()
        except tk.TclError as e:
            print(f"Error: {e}")

# class Product:
#     def __init__(self, name, price, image):
#         self.name = name
#         self.price = price
#         self.image = image

# List of products
# products = [
#     Product("Product 1", 10.99, "product1.jpg"),
#     Product("Product 2", 15.99, "product2.jpg"),
#     Product("Product 3", 20.99, "product3.jpg"),
#     # Add more products as needed
# ]

# def add_to_cart(product, quantity):
#     print(f"Added {quantity} {product.name} to cart.")

# Create the main window
root = tk.Tk()
root.title("Product Catalog")

image_paths = ["images/burger.png", "images/burger.png", "images/burger.png"]

# Resize factor
resize_factor = 2

# Display resized images
display_resized_images(root, image_paths, resize_factor)

# # Create a frame for products
# product_frame = tk.Frame(root)
# product_frame.pack(padx=10, pady=10)

# Populate the frame with products
# for product in products:
#     # Product Image
#     image_label = tk.Label(product_frame, text=f"Image: {product.image}")
#     image_label.grid(row=products.index(product), column=0)

#     # Product Name
#     name_label = tk.Label(product_frame, text=f"Name: {product.name}")
#     name_label.grid(row=products.index(product), column=1)

#     # Product Price
#     price_label = tk.Label(product_frame, text=f"Price: ${product.price}")
#     price_label.grid(row=products.index(product), column=2)

#     # Quantity Spinbox
#     quantity_spinbox = tk.Spinbox(product_frame, from_=0, to=10, width=5)
#     quantity_spinbox.grid(row=products.index(product), column=3)

#     # Button to add to cart
#     add_to_cart_button = tk.Button(product_frame, text="Add to Cart",
#     command=lambda p=product, q=quantity_spinbox: add_to_cart(p, q.get()))
#     add_to_cart_button.grid(row=products.index(product), column=4)


# burger = tk.PhotoImage(file="images/burger.png")
# burger_label = tk.Label(image=burger,borderwidth=0)
# burger_label.place(x=50,y=130)
# burger_info = tk.Label(text="Burgir", font=("Times New Roman", 10, "normal"), bg="tomato")
# burger_info.place(x=40,y=230)
# burger_sb = tk.Spinbox(from_=0, to=100, width=5)
# burger_sb.place(x=80,y=270) 

image_paths = ["images/burger.png", "images/burger.png", "images/burger.png"]

# Resize factor
resize_factor = 2

# Display resized images
display_resized_images(root, image_paths, resize_factor)
root.mainloop()
