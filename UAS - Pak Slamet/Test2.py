import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox

# Sample menu data
menu = [
    {"id": 1, "nama": "Ayam-Bakar", "harga": 50000, "image": "Resource/AB.jpg"},
    {"id": 2, "nama": "Nasi-Goreng", "harga": 75000, "image": "Resource/NG.jpg"},
    {"id": 3, "nama": "Es-Teh", "harga": 60000, "image": "Resource/ET.jpg"},
]

pesanan = []  # To store orders
fig, ax = plt.subplots(figsize=(8, 6))


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


def clear_all_content(event):
    """Clears the entire figure, including buttons, images, and text."""
    plt.clf()  # Clear the figure
    plt.draw()  # Redraw the cleared figure


def pelanggan():
    plt.clf()  # Clear any previous content
    ax = fig.add_subplot(1, 1, 1)  # Re-add subplot
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
    table_number_box = TextBox(table_number_ax, "Table No:", initial="")

    food_id_ax = plt.axes([0.4, 0.2, 0.2, 0.05])
    food_id_box = TextBox(food_id_ax, "Food ID:", initial="")

    quantity_ax = plt.axes([0.7, 0.2, 0.2, 0.05])
    quantity_box = TextBox(quantity_ax, "Quantity:", initial="")

    # Submit button
    submit_ax = plt.axes([0.4, 0.1, 0.2, 0.05])
    submit_button = Button(submit_ax, "Submit Order")
    submit_button.on_clicked(submit_order)

    # Clear button
    clear_ax = plt.axes([0.7, 0.1, 0.2, 0.05])
    clear_button = Button(clear_ax, "Clear All")
    clear_button.on_clicked(clear_all_content)

    plt.draw()  # Update the display


# Display the initial menu
pelanggan()
plt.show()
