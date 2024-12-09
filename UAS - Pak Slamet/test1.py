import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox

# Sample menu data
menu = [
    {"id": 1, "nama": "Ayam-Bakar", "harga": 50000, "image": "Resource/AB.jpg"},
    {"id": 2, "nama": "Nasi-Goreng", "harga": 75000, "image": "Resource/NG.jpg"},
    {"id": 3, "nama": "Es-Teh", "harga": 60000, "image": "Resource/ET.jpg"},
]

pesanan = []  # To store orders

def clear_all_content():
    """Clears the entire figure, including widgets."""
    for child in fig.get_children():  # Get all child objects of the figure
        if isinstance(child, plt.Axes):  # Check if the child is an Axes object
            child.remove()  # Remove the Axes object
    plt.draw()  # Redraw the figure

def submit_order(event):
    nomor_meja = table_number_box.text
    pilihan = food_id_box.text
    jumlah = quantity_box.text

    if not nomor_meja or not pilihan or not jumlah:
        print("Please fill in all fields!")
        return

    try:
        pilihan = int(pilihan)
        jumlah = int(jumlah)
        for item in menu:
            if item["id"] == pilihan:
                pesanan.append({"meja": nomor_meja, "menu": item, "jumlah": jumlah})
                print(f"Pesanan {item['nama']} untuk meja {nomor_meja} berhasil dibuat.")
                return
        print("Invalid food ID!")
    except ValueError:
        print("Invalid input! Please enter numbers for food ID and quantity.")


def pelanggan(users):
    clear_all_content()
    ax.axis("off")

    # Display menu items
    for i, item in enumerate(menu):
        img_ax = fig.add_axes([0.1 + i * 0.3, 0.5, 0.2, 0.3])  # Position for each image
        img = plt.imread(item["image"])  # Load image
        img_ax.imshow(img)
        img_ax.axis("off")
        ax.text(0.2 + i * 0.3, 0.45, f"{item['nama']}\nRp{item['harga']}", ha="center", fontsize=10)

    # Input fields
    global table_number_box, food_id_box, quantity_box
    table_number_ax = plt.axes([0.1, 0.2, 0.2, 0.05])
    table_number_box = TextBox(table_number_ax, "Table No:")

    food_id_ax = plt.axes([0.4, 0.2, 0.2, 0.05])
    food_id_box = TextBox(food_id_ax, "Food ID:")

    quantity_ax = plt.axes([0.7, 0.2, 0.2, 0.05])
    quantity_box = TextBox(quantity_ax, "Quantity:")

    # Submit button
    submit_ax = plt.axes([0.4, 0.1, 0.2, 0.05])
    submit_button = Button(submit_ax, "Submit Order")
    submit_button.on_clicked(submit_order)

    fig.canvas.draw_idle()

def login_gui(users):
    print(f"Login GUI opened with users: {users}")
    ax.clear()  # Clear the existing content
    ax.axis("off")
    ax.text(0.5, 0.5, "Login Page", ha="center", va="center", fontsize=16)
    fig.canvas.draw_idle()  # Update the canvas

def exit_program(event):
    print("Exiting program...")
    plt.close('all')  # Closes all matplotlib windows

# Main page
def main_page(users):
    global fig, ax
    fig, ax = plt.subplots(figsize=(6, 4))  # Create a single figure
    ax.axis("off")  # Hide the axes

    # Display the main menu
    ax.text(0.5, 0.7, "Main Menu", ha="center", va="center", fontsize=20)

    # Create buttons
    button1_ax = plt.axes([0.1, 0.1, 0.2, 0.1])  # [left, bottom, width, height]
    button1 = Button(button1_ax, 'Pelanggan')
    button1.on_clicked(pelanggan)

    button2_ax = plt.axes([0.4, 0.1, 0.2, 0.1])
    button2 = Button(button2_ax, 'Login')
    button2.on_clicked(lambda event: login_gui(users))

    button3_ax = plt.axes([0.7, 0.1, 0.2, 0.1])
    button3 = Button(button3_ax, 'Exit')
    button3.on_clicked(exit_program)

    plt.show()

# Example usage
users = ["User1", "User2"]
main_page(users)
