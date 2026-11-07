class RekeningBank:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo              # privat

    @property
    def saldo(self):                      # akses saldo (read-only)
        return self.__saldo

    def setor(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah setor harus positif.")
        self.__saldo += jumlah

    def tarik(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah tarik harus positif.")
        if jumlah > self.__saldo:
            raise ValueError("Saldo tidak cukup.")
        self.__saldo -= jumlah

    def tampilkan_saldo(self):
        print(f"Saldo {self.pemilik}: Rp{self.__saldo}")


# Program utama
rek = RekeningBank("raihan", 100000)
rek.tampilkan_saldo()                     # Saldo raihan: Rp100000

# 1. Setor uang
rek.setor(50000)
rek.tampilkan_saldo()                     # Saldo raihan: Rp150000

# 2. Tarik uang yang valid
rek.tarik(30000)
rek.tampilkan_saldo()                     # Saldo raihan: Rp120000

# 3. Tarik melebihi saldo (harus ditolak)
try:
    rek.tarik(500000)
except ValueError as e:
    print("Ditolak:", e)                  # Ditolak: Saldo tidak cukup.

# 4. Tarik jumlah negatif (harus ditolak)
try:
    rek.tarik(-1000)
except ValueError as e:
    print("Ditolak:", e)                  # Ditolak: Jumlah tarik harus positif.

rek.tampilkan_saldo()                     # Saldo raihan: Rp120000 (tidak berubah)