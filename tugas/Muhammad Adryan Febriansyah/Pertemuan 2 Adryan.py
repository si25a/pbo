
"""Latihan Individu Pertemuan 2 - Class KartuMahasiswa."""


class KartuMahasiswa:
    def __init__(self, nama, nim, saldo):
        self.nama = nama
        self.nim = nim
        self.saldo = saldo

    def isi_saldo(self, jumlah):
        self.saldo += jumlah
        print(f"Berhasil mengisi saldo sebesar Rp{jumlah}.")

    def gunakan_saldo(self, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
            print(f"Berhasil menggunakan saldo sebesar Rp{jumlah}.")
            return True
        else:
            print("Saldo tidak mencukupi!")
            return False

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Saldo: Rp{self.saldo}")


if __name__ == "__main__":
    kartu = KartuMahasiswa("Badar", "SI2026001", 50000)

    kartu.tampilkan_info()

    kartu.isi_saldo(25000)
    kartu.tampilkan_info()

    kartu.gunakan_saldo(30000)
    kartu.tampilkan_info()

    kartu.gunakan_saldo(100000)
    kartu.tampilkan_info()
