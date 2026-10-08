class KartuMahasiswa:
    """Latihan class object dengan method perubahan data."""

    def __init__(self, nama, nim, saldo):
        # Menyimpan nama, nim, dan saldo sebagai attribute instance
        self.nama = nama
        self.nim = nim
        self.saldo = saldo

    def isi_saldo(self, jumlah):
        # Menambahkan jumlah ke saldo jika valid
        if jumlah > 0:
            self.saldo += jumlah
            print(f"Berhasil isi saldo sebesar {jumlah}.")
        else:
            print("Jumlah isi saldo harus lebih besar dari 0.")

    def gunakan_saldo(self, jumlah):
        # Kurangi saldo jika saldo mencukupi dan kembalikan True
        if 0 < jumlah <= self.saldo:
            self.saldo -= jumlah
            print(f"Berhasil menggunakan saldo sebesar {jumlah}.")
            return True
        else:
            print("Gagal menggunakan saldo: Saldo tidak mencukupi atau jumlah tidak valid.")
            return False

    def tampilkan_info(self):
        # Cetak nama, nim, dan saldo
        print(f"Nama  : {self.nama}")
        print(f"NIM   : {self.nim}")
        print(f"Saldo : {self.saldo}")
        print("-" * 25)


if __name__ == "__main__":
    kartu = KartuMahasiswa("Roziah", "SI-102", 20000)
    kartu.tampilkan_info()
    kartu.isi_saldo(10000)
    kartu.gunakan_saldo(15000)
    kartu.tampilkan_info()
