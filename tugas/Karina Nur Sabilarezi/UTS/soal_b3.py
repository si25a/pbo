
# SOAL B3 - ANALISIS DAN PERBAIKAN KODE

class RekeningBank:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.__saldo = saldo

    # Property untuk membaca saldo
    @property
    def saldo(self):
        return self.__saldo

    # Method untuk menyetor uang
    def setor(self, jumlah):
        if jumlah <= 0:
            return False
        else:
            self.__saldo += jumlah
            return True

    # Method untuk menarik uang
    def tarik(self, jumlah):
        if jumlah <= 0:
            return False
        elif jumlah > self.__saldo:
            return False
        else:
            self.__saldo -= jumlah
            return True

    # Method untuk menampilkan saldo
    def tampilkan_saldo(self):
        print(f"Saldo {self.pemilik}: Rp{self.__saldo}")


# PROGRAM UTAMA

# Membuat object rekening bank
rekening = RekeningBank("Andi", 500000)

# Menampilkan saldo awal
print("Saldo Awal:")
rekening.tampilkan_saldo()

# 1. Melakukan setor uang
print("\n1. Setor uang Rp200000")
if rekening.setor(200000):
    print("Setor uang berhasil.")
else:
    print("Setor uang ditolak.")

rekening.tampilkan_saldo()

# 2. Melakukan penarikan uang yang valid
print("\n2. Tarik uang Rp100000")
if rekening.tarik(100000):
    print("Penarikan berhasil.")
else:
    print("Penarikan ditolak.")

rekening.tampilkan_saldo()

# 3. Melakukan penarikan melebihi saldo
print("\n3. Tarik uang Rp1000000")
if rekening.tarik(1000000):
    print("Penarikan berhasil.")
else:
    print("Penarikan ditolak: saldo tidak mencukupi.")

rekening.tampilkan_saldo()

# 4. Melakukan penarikan dengan jumlah negatif
print("\n4. Tarik uang Rp-50000")
if rekening.tarik(-50000):
    print("Penarikan berhasil.")
else:
    print("Penarikan ditolak: jumlah harus positif.")

rekening.tampilkan_saldo()
