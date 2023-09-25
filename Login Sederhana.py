# Membuat sebuah dictionary untuk menyimpan data pengguna (nama, NIM, dan tanggal lahir)
database_pengguna = {
    "user1": {
        "nama": "Muhammad Danil Pratama",
        "nim": "2309116091",
        "tgl_lahir": "01-01-2000"
    },
    "user2": {
        "nama": "Asep Gaming",
        "nim": "999999999",
        "tgl_lahir": "09-09-1999"
    }
}

# Fungsi untuk melakukan login
def login():
    # Minta pengguna memasukkan NIM dan tanggal lahir
    nim = input("Masukkan NIM: ")
    tgl_lahir = input("Masukkan tanggal lahir (tgl-bulan-tahun): ")

    # Cek apakah NIM dan tanggal lahir sesuai dengan yang ada di database
    for username, data in database_pengguna.items():
        if data["nim"] == nim and data["tgl_lahir"] == tgl_lahir:
            print(f"Selamat datang, {data['nama']}!")
            return
    print("NIM atau tanggal lahir salah. Silakan coba lagi.")

# Memanggil fungsi login
login()
