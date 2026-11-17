
class RekeningBank:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print("Setor berhasil.")
        else:
            print("Jumlah setor harus positif.")

    def tarik(self, jumlah):
        if jumlah <= 0:
            print("Jumlah penarikan harus positif.")
        elif jumlah > self.__saldo:
            print("Saldo tidak mencukupi.")
        else:
            self.__saldo -= jumlah
            print("Penarikan berhasil.")

    def tampilkan_saldo(self):
        print(f"Saldo {self.pemilik}: Rp{self.__saldo}")


# Program utama
rekening = RekeningBank("Budi", 500000)

# Menampilkan saldo awal
rekening.tampilkan_saldo()

# Setor uang
rekening.setor(200000)
rekening.tampilkan_saldo()

# Tarik uang yang valid
rekening.tarik(100000)
rekening.tampilkan_saldo()

# Tarik uang melebihi saldo
rekening.tarik(1000000)
rekening.tampilkan_saldo()

# Tarik jumlah negatif
rekening.tarik(-50000)
rekening.tampilkan_saldo()
