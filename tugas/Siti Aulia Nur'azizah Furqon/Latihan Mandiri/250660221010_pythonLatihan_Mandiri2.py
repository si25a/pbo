class KartuMahasiswa:

    def __init__(self, nama, nim, saldo):
        # menyimpan nama, nim, dan saldo sebagai attribute.
        self.nama = nama
        self.nim = nim
        self.saldo = saldo
        pass

    def isi_saldo(self, jumlah):
        # menambahkan jumlah ke saldo.
        self.saldo += jumlah
        pass

    def gunakan_saldo(self, jumlah):
        # mengurangi saldo jika saldo mencukupi dan kembalikan True
        if self.saldo >= jumlah:
            self.saldo -= jumlah
            return True
        else:
            return False
        pass

    def tampilkan_info(self):
        # print nama, nim, dan saldo.
        print(f"Nama: {self.nama}, NIM: {self.nim}, Saldo: {self.saldo}")
        pass


if __name__ == "__main__":
    kartu = KartuMahasiswa("Ani Lestari", "SI-102", 20000)
    kartu.tampilkan_info()
    kartu.isi_saldo(10000)
    kartu.gunakan_saldo(15000)
    kartu.tampilkan_info()
