"""
Soal A2 - Pilar OOP

Jelaskan keempat pilar OOP berikut beserta penggunaannya pada program Python:
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction
Untuk setiap pilar, sertakan satu contoh kode singkat yang menunjukkan penerapannya.

Jawaban:
1. Encapsulation adalah konsep membungkus data (atribut) dan method dalam satu unit (class)
    serta menyembunyikan detail akses langsung dari luar menggunakan atribut privat (diawali __). Ini berguna untuk menjaga integritas data agar tidak diubah sembarangan.
2. Inheritance adalah mekanisme di mana sebuah class (subclass/child) dapat mewarisi atribut dan method dari class lain (superclass/parent).
    Mengurangi duplikasi kode dan mempermudah reusability.
3. Polymorphism merupakan kemampuan berbagai class yang berbeda untuk merespons pemanggilan method yang sama dengan cara/implementasi yang berbeda.
4. Abstraction adalah konsep menyembunyikan detail kompleksitas implementasi dan hanya menampilkan fungsi/fitur penting kepada pengguna (menggunakan modul abc di Python).

Berikut Contoh kode singkat masing masing pilar:
"""
# 1. Encapsulation
class AkunShopee:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atribut privat

    def get_saldo(self):
        return self.__saldo

# 2. Inheritance
class Produk:
    def __init__(self, nama):
        self.nama = nama

class ProdukDigital(Produk):  # Mewarisi Produk
    def unduh(self):
        return f"Mengunduh {self.nama}"

# 3. Polymorphism
class DiskonPersen:
    def hitung(self, harga):
        return harga * 0.9

class DiskonNominal:
    def hitung(self, harga):
        return harga - 10000
# Kedua class memiliki method 'hitung' yang sama namun perilakunya berbeda.

# 4. Abstraction
from abc import ABC, abstractmethod

class Pembayaran(ABC):
    @abstractmethod
    def proses(self):
        pass

class TransferBank(Pembayaran):
    def proses(self):
        return "Memproses transfer bank..."