def cetak_pola_segitiga():
    try:
        # Meminta pengguna memasukkan jumlah baris
        jumlah_baris = int(input("Masukkan jumlah baris: "))

        # Validasi input
        if jumlah_baris <= 0:
            print("Jumlah baris harus bilangan positif.")
            return

        # Mencetak pola segitiga
        for i in range(1, jumlah_baris + 1):
            print("*" * i)
    except ValueError:
        print("Harap masukkan bilangan bulat yang valid.")

# Memanggil fungsi
cetak_pola_segitiga()
