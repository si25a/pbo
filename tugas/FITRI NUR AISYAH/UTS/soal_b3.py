class RekeningBank:
    def __init__(self, pemilik, saldo=0):
        self.__pemilik = pemilik
        self.__saldo = saldo

    @property
    def pemilik(self):
        return self.__pemilik

    @property
    def saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah <= 0:
            return False
        self.__saldo += jumlah
        return True

    def tarik(self, jumlah):
        if jumlah <= 0:
            return False
        if jumlah > self.__saldo:
            return False
        self.__saldo -= jumlah
        return True

    def tampilkan_saldo(self):
        print(f"Saldo {self.__pemilik}: Rp{self.__saldo}")


if __name__ == "__main__":
    rek = RekeningBank("Budi", 100000)
    rek.tampilkan_saldo()

    print("Setor 50000:", "Berhasil" if rek.setor(50000) else "Ditolak")
    rek.tampilkan_saldo()

    print("Tarik 30000:", "Berhasil" if rek.tarik(30000) else "Ditolak")
    rek.tampilkan_saldo()

    print("Tarik 500000:", "Berhasil" if rek.tarik(500000) else "Ditolak (saldo tidak cukup)")
    rek.tampilkan_saldo()

    print("Tarik -2000:", "Berhasil" if rek.tarik(-2000) else "Ditolak (jumlah harus positif)")
    rek.tampilkan_saldo()
