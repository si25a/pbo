class KartuMahasiswa:
    def __init__(self, nama, nim, saldo):
        self.nama = nama
        self.nim = nim
        self.saldo = saldo

    def isi_saldo(self, jumlah):
        self.saldo += jumlah

    def gunakan_saldo(self, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
            return True
        else:
            return False

    def tampilkan_info(self):
        print("Nama  :", self.nama)
        print("NIM   :", self.nim)
        print("Saldo :", self.saldo)


# Contoh penggunaan
kartu = KartuMahasiswa("Jihan Maharani", "250660221031", 100000)

kartu.tampilkan_info()

kartu.isi_saldo(50000)
print("\nSetelah isi saldo:")
kartu.tampilkan_info()

hasil = kartu.gunakan_saldo(30000)
print("\nPenggunaan saldo berhasil:", hasil)
kartu.tampilkan_info()

hasil = kartu.gunakan_saldo(200000)
print("\nPenggunaan saldo berhasil:", hasil)
kartu.tampilkan_info()