# UTS PBO Bagian B — Coding dan Problem Solving
# Soal B3 — Analisis dan Perbaikan Kode

class RekeningBank:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik

        # PERBAIKAN:
        # Attribute saldo dibuat privat untuk menerapkan encapsulation.
        self.__saldo = saldo

    # PROPERTY
    # Digunakan untuk mengakses saldo tanpa mengubahnya secara langsung.
    @property
    def saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        # PERBAIKAN MASALAH 2:
        # Kode awal tidak memiliki validasi setoran.
        # Jumlah setoran harus lebih dari nol.
        if jumlah <= 0:
            print("Setoran harus lebih dari nol.")
            return False

        self.__saldo += jumlah
        print(f"Berhasil setor Rp{jumlah}")
        return True

    def tarik(self, jumlah):
        # PERBAIKAN MASALAH 3:
        # Kode awal tidak memiliki validasi penarikan.
        # Jumlah penarikan harus positif.
        if jumlah <= 0:
            print("Penarikan harus lebih dari nol.")
            return False

        # Penarikan tidak boleh melebihi saldo.
        if jumlah > self.__saldo:
            print("Saldo tidak mencukupi.")
            return False

        self.__saldo -= jumlah
        print(f"Berhasil tarik Rp{jumlah}")
        return True

    def tampilkan_saldo(self):
        print(f"Saldo {self.pemilik}: Rp{self.__saldo}")


# IDENTIFIKASI 3 MASALAH PADA KODE AWAL:
#
# 1. Attribute saldo masih bersifat publik (self.saldo),
#    sehingga dapat diakses dan diubah langsung dari luar class.
#    Hal ini tidak menerapkan encapsulation.
#
# 2. Method setor() tidak memiliki validasi jumlah setoran.
#    Akibatnya, jumlah negatif atau nol tetap dapat diproses.
#
# 3. Method tarik() tidak memiliki validasi penarikan.
#    Akibatnya, penarikan dapat melebihi saldo atau menggunakan
#    jumlah negatif sehingga saldo menjadi tidak sesuai.


# PROGRAM UTAMA
rekening = RekeningBank("Andi", 1000000)

# Menampilkan saldo awal
rekening.tampilkan_saldo()

# Melakukan setor uang
rekening.setor(500000)

# Melakukan penarikan yang valid
rekening.tarik(200000)

# Melakukan penarikan melebihi saldo
rekening.tarik(2000000)

# Melakukan penarikan jumlah negatif
rekening.tarik(-100000)

# Menampilkan saldo akhir
rekening.tampilkan_saldo()