# Encapsulation
class AkunBank:
    def __init__(self, saldo_awal):
        self.__saldo = saldo_awal  # Atribut privat

    # Getter untuk mengakses data privat secara aman
    def get_saldo(self):
        return self.__saldo

# Contoh penggunaan:
akun = AkunBank(500000)
print(akun.get_saldo())  # Output: 500000
# print(akun.__saldo)    # Error (tidak bisa diakses langsung)


# Inheritance
class Kendaraan:  # Parent class
    def __init__(self, merek):
        self.merek = merek

    def klakson(self):
        return "Biot!"

class Mobil(Kendaraan):  # Subclass mewarisi Kendaraan
    def buka_pintu(self):
        return "Pintu dibuka."

# Contoh penggunaan:
civic = Mobil("Honda")
print(civic.merek)      # Output: Honda (diwarisi dari parent)
print(civic.klakson())  # Output: Biot! (diwarisi dari parent)


# Polymorphism
class Kucing:
    def bersuara(self):
        return "Meow!"

class Anjing:
    def bersuara(self):
        return "Guk Guk!"

def cetak_suara(hewan):
    print(hewan.bersuara())

# Contoh penggunaan (menerima tipe objek berbeda tanpa pengecekan):
cetak_suara(Kucing())  # Output: Meow!
cetak_suara(Anjing())  # Output: Guk Guk!


# Abstraction
from abc import ABC, abstractmethod

class Pembayaran(ABC):  # Class abstrak
    @abstractmethod
    def proses_bayar(self, jumlah):
        pass

class TransferBank(Pembayaran):
    def proses_bayar(self, jumlah):
        return f"Membayar Rp{jumlah} via Transfer Bank."

# Contoh penggunaan:
# pb = Pembayaran()  # Error: tidak bisa di-instansiasi langsung
bayar = TransferBank()
print(bayar.proses_bayar(100000))  # Output: Membayar Rp100000 via Transfer Bank.