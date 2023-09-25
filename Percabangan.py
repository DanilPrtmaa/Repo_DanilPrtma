# Meminta pengguna untuk memilih mata uang
print("mata uang yang dikonversikan")
print("USD - Dolar Amerika Serikat")
print("Yen - Yan Jepang")
print("Ringgit malaysia")

# Pilihan Pengguna
pilihan = int(input("Masukan nomor (1/2/3): "))

# Menggunakan percabangan if untuk melakukan konversi berdasarkan pilihan pengguna
jumlah_dolar = float(input("masukkan jumlah dolar "))

if pilihan == 1:
    hasil_konversi = jumlah_dolar
    mata_uang_tujuan = "USD"
elif pilihan == 2:
    hasil_konversi = jumlah_dolar * 'nilai_tukar_usd_ke_yen' # Gantilah dengan nilai tukar yang sesuai
    mata_uang_tujuan = "Yen"
elif pilihan == 3:
    hasil_konversi = jumlah_dolar * 'nilai_tukar_usd_ke_ringgit' # Gantilah dengan nilai tukar yang sesuai
    mata_uang_tujuan = "Ringgit Malaysia"
else:
    print("Pilihan tidak valid")

# Menampilkan hasil konversi
if pilihan in [1, 2, 3]:
    print(f"{jumlah_dolar} USD setara dengan {hasil_konversi} {mata_uang_tujuan}")