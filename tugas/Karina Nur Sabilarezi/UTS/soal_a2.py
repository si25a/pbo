
# SOAL A2 - PILAR OOP

from abc import ABC, abstractmethod


# 1. ENCAPSULATION
# Encapsulation adalah konsep untuk melindungi data
# agar tidak dapat diakses atau diubah sembarangan dari luar class.
# Penggunaannya dalam Python yaitu dengan attribute privat
# dan property untuk mengatur akses terhadap data.

class Mahasiswa:
    def __init__(self, nama):
        self.__nama = nama

    @property
    def nama(self):
        return self.__nama


# 2. INHERITANCE
# Inheritance adalah konsep pewarisan attribute dan method
# dari class induk kepada class turunan.
# Penggunaannya untuk menggunakan kembali kode dari class induk.

class Hewan:
    def makan(self):
        print("Hewan sedang makan")


class Kucing(Hewan):
    pass


# 3. POLYMORPHISM
# Polymorphism adalah kemampuan beberapa object berbeda
# untuk menggunakan method yang sama dengan perilaku berbeda.
# Penggunaannya untuk membuat program lebih fleksibel.

class KucingSuara:
    def bersuara(self):
        print("Meong")


class Anjing:
    def bersuara(self):
        print("Guk guk")


# 4. ABSTRACTION
# Abstraction adalah konsep menyembunyikan detail proses
# dan hanya menampilkan fungsi utama yang diperlukan.
# Penggunaannya untuk menentukan method yang harus
# dibuat oleh class turunan.

class Kendaraan(ABC):
    @abstractmethod
    def berjalan(self):
        pass


class Mobil(Kendaraan):
    def berjalan(self):
        print("Mobil sedang berjalan")


# PROGRAM UTAMA

# Contoh Encapsulation
mahasiswa1 = Mahasiswa("Andi")
print("Contoh Encapsulation:", mahasiswa1.nama)

# Contoh Inheritance
kucing1 = Kucing()
print("Contoh Inheritance:")
kucing1.makan()

# Contoh Polymorphism
kucing2 = KucingSuara()
anjing1 = Anjing()

daftar_hewan = [kucing2, anjing1]

print("Contoh Polymorphism:")
for hewan in daftar_hewan:
    hewan.bersuara()

# Contoh Abstraction
mobil1 = Mobil()
print("Contoh Abstraction:")
mobil1.berjalan()
