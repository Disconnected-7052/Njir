import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button
import csv
import numpy as np
import os

# Global variables
menu = [
    {"id": 1, "nama": "Nasi Goreng", "harga": 20000},
    {"id": 2, "nama": "Ayam Bakar", "harga": 25000},
    {"id": 3, "nama": "Es Teh", "harga": 5000}
]
pesanan = []
laporan_penjualan = []

# Function to read credentials from CSV
def load_users_from_csv(filename):
    users = {}
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    users[row[0]] = row[1]
    return users

# Fungsi untuk pelanggan (Tanpa login)
def pelanggan():
    print("=== Menu Pelanggan ===")
    nomor_meja = input("Masukkan nomor meja: ")
    print("Daftar Menu:")
    for item in menu:
        print(f"{item['id']}. {item['nama']} - Rp{item['harga']}")

    pilihan = int(input("Pilih menu (masukkan ID): "))
    jumlah = int(input("Masukkan jumlah: "))

    for item in menu:
        if item["id"] == pilihan:
            pesanan.append({"meja": nomor_meja, "menu": item, "jumlah": jumlah})
            print(f"Pesanan {item['nama']} untuk meja {nomor_meja} berhasil dibuat.")
            break

# Fungsi untuk kasir
def kasir():
    print("=== Menu Kasir ===")
    print("Pesanan Saat Ini:")
    total = 0
    for p in pesanan:
        subtotal = p["menu"]["harga"] * p["jumlah"]
        total += subtotal
        print(f"Meja {p['meja']}: {p['menu']['nama']} x {p['jumlah']} = Rp{subtotal}")

    print(f"Total: Rp{total}")
    metode_bayar = input("Metode Pembayaran (Tunai/Kartu/QRIS): ")
    laporan_penjualan.append({"total": total, "metode": metode_bayar})
    print("Pembayaran berhasil!")

# Fungsi untuk admin
def admin(users, filename):
    while True:
        print("=== Menu Admin ===")
        print("1. Tambah Menu")
        print("2. Hapus Menu")
        print("3. Update Menu")
        print("4. Kelola Pegawai")
        print("5. Kembali")

        pilihan = int(input("Pilih menu: "))

        if pilihan == 1:
            nama = input("Masukkan nama menu: ")
            harga = int(input("Masukkan harga menu: "))
            menu.append({"id": len(menu) + 1, "nama": nama, "harga": harga})
            print(f"Menu {nama} berhasil ditambahkan.")
        elif pilihan == 2:
            hapus_id = int(input("Masukkan ID menu yang ingin dihapus: "))
            menu[:] = [item for item in menu if item["id"] != hapus_id]
            print("Menu berhasil dihapus.")
        elif pilihan == 3:
            update_id = int(input("Masukkan ID menu yang ingin diupdate: "))
            for item in menu:
                if item["id"] == update_id:
                    item["nama"] = input("Masukkan nama baru: ")
                    item["harga"] = int(input("Masukkan harga baru: "))
                    print("Menu berhasil diupdate.")
                    break
        elif pilihan == 4:
            kelola_pegawai(users, filename)  # Panggil fungsi Kelola Pegawai
        elif pilihan == 5:
            break

# Fungsi untuk kelola pegawai
def kelola_pegawai(users, filename):
    print("=== Kelola Pegawai ===")
    print("1. Tambah Pegawai")
    print("2. Hapus Pegawai")
    print("3. Ubah Password Pegawai")
    print("4. Kembali")
    
    pilihan = int(input("Pilih menu: "))
    
    if pilihan == 1:
        username = input("Masukkan username pegawai baru: ")
        password = input("Masukkan password pegawai baru: ")
        users[username] = password
        print(f"Pegawai {username} berhasil ditambahkan.")
        save_users_to_csv(users, filename)
    elif pilihan == 2:
        username = input("Masukkan username pegawai yang ingin dihapus: ")
        if username in users:
            del users[username]
            print(f"Pegawai {username} berhasil dihapus.")
            save_users_to_csv(users, filename)
        else:
            print(f"Pegawai {username} tidak ditemukan.")
    elif pilihan == 3:
        username = input("Masukkan username pegawai yang ingin diubah password-nya: ")
        if username in users:
            new_password = input("Masukkan password baru: ")
            users[username] = new_password
            print(f"Password pegawai {username} berhasil diubah.")
            save_users_to_csv(users, filename)
        else:
            print(f"Pegawai {username} tidak ditemukan.")
    elif pilihan == 4:
        return

# Fungsi untuk menyimpan data pengguna ke CSV
def save_users_to_csv(users, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for username, password in users.items():
            writer.writerow([username, password])

# Fungsi untuk pelayan
def pelayan():
    print("=== Menu Pelayan ===")
    if not pesanan:
        print("Belum ada pesanan dari pelanggan.")
    else:
        print("Daftar Pesanan Pelanggan:")
        for idx, p in enumerate(pesanan, 1):
            print(f"{idx}. Meja {p['meja']} - {p['menu']['nama']} x {p['jumlah']}")

        konfirmasi = input("Konfirmasi pesanan? (y/n): ").lower()
        if konfirmasi == "y":
            print("Pesanan berhasil diterima.")
        else:
            print("Pesanan tidak dikonfirmasi.")

# GUI Login
def login_gui(users):
    def on_login(event):
        global current_user
        username = username_box.text.strip()
        password = password_box.text.strip()

        if username in users and users[username] == password:
            current_user = username
            plt.close(fig)  # Menutup GUI login
            print(f"Login berhasil sebagai {username}")
            if username == "kasir":
                kasir()
            elif username == "admin":
                admin(users, 'Data.csv')
            elif username == "owner":
                owner()
            elif username == "pelayan":
                pelayan()
        else:
            result_box.set_val("Login Gagal!")

    fig, ax = plt.subplots(figsize=(6, 4))
    plt.subplots_adjust(bottom=0.4)
    ax.axis('off')

    # TextBox untuk Username
    ax_username = plt.axes([0.2, 0.65, 0.6, 0.1])
    username_box = TextBox(ax_username, "Username: ")

    # TextBox untuk Password
    ax_password = plt.axes([0.2, 0.45, 0.6, 0.1])
    password_box = TextBox(ax_password, "Password: ")

    # Tombol Login
    ax_button = plt.axes([0.4, 0.25, 0.2, 0.1])
    button = Button(ax_button, "Login")
    button.on_clicked(on_login)

    # Kotak hasil
    ax_result = plt.axes([0.2, 0.1, 0.6, 0.1])
    result_box = TextBox(ax_result, "", initial="")

    plt.show()

# Program utama
def main():
    users = load_users_from_csv('Data.csv')
    if not users:
        print("Tidak ada data pengguna untuk login. Program dihentikan.")
        return

    while True:
        print("=== Sistem Restoran ===")
        print("1. Pelanggan (Tidak Perlu Login)")
        print("2. Login Kasir/Admin/Owner/Pelayan")
        print("3. Keluar")

        pilihan = int(input("Pilih menu: "))
        if pilihan == 1:
            pelanggan()
        elif pilihan == 2:
            login_gui(users)
        elif pilihan == 3:
            print("Terima kasih telah menggunakan sistem.")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program utama
if 1 == 1:
    main()